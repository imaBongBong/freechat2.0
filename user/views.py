from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import Profile
from base.models import Topic,UserMessage,Room
from .forms import CustomUserCreationForm,ProfileForm
# Create your views here.
def user_login(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_username = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist.')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'username or password does not correct')
    context = {'page':page}
    return render(request,'user/login_register.html',context)


def user_register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request,user)
            messages.success(request,"User created")
            return redirect('index')
    context = {'form':form}
    return render(request,'user/login_register.html',context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,'logout success!')
    return redirect('index')

def user_profile(request,pk):
    topics = Topic.objects.all()
    profile = Profile.objects.get(id=pk)
    messages = profile.usermessage_set.all()
    rooms = profile.room_set.all()
    context = {'profile':profile,'topics':topics,'messages':messages,'rooms':rooms}
    return render(request,'user/profile.html',context)

@login_required(login_url='login')
def update_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile',profile.id)
    context = {'form':form}
    return render(request,'user/update_profile.html',context)
