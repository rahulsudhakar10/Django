from django.shortcuts import render
from basic_app import forms
#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"basic_app/index.html")

@login_required
def special(request):
    return HttpResponse("only logged in")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registeration =True

    if request.method == "POST":

        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfieInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
        else:
            print(user_form.errors,profile_form.errors)
    else:
        registeration =False
        user_form = forms.UserForm()
        profile_form = forms.UserProfieInfo()
    return render(request,'basic_app/register.html',
              {'registered':registeration,
              'user_info':user_form,
              'profile_info':profile_form})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('User is Not Active')
        else:
            print("Someon tried login")
            return HttpResponse('InValid login')
    else:
        return render(request,'basic_app/login.html')
