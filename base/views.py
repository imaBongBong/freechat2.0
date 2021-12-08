from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room, Topic,UserMessage
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    messages = UserMessage.objects.all()
    q = request.GET.get('q')
    if q is not None:
        rooms = Room.objects.filter(Q(name__icontains=q)|Q(topic__name__icontains=q))
    context = {'rooms':rooms,'topics':topics[:5],'messages':messages[:5]}
    return render(request,'base/index.html',context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()
    profile = request.user.profile
    if request.method == "POST":
        form = RoomForm(request.POST)
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            name = request.POST.get('name'),
            topic = topic,
            owner = request.user.profile,
            description = request.POST.get('description'),
        )
        return redirect('index')
    context = {'form':form,'topics':topics}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.user.profile.id != room.owner.id:
        #检测到当前用户不是房间的拥有者 将用户直接重新定向
        return HttpResponse('you are not allow here!')
    obj = room.name
    if request.method == "POST":
        room.delete()
        return redirect('index')
    context = {'obj':obj}
    return render(request,'delete.html',context)
    

@login_required(login_url='login')
def edit_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.user.profile.id != room.owner.id:
    #检测到当前用户不是房间的拥有者 将用户直接重新定向
        return HttpResponse('you are not allow here!')
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form,'topics':topics}
    return render(request,'base/room_form.html',context)

def single_room(request,pk):
    room = Room.objects.get(id=pk)
    participants = room.participants.all()
    messages = room.usermessage_set.all()
    print(participants)
    if request.method == "POST":
        message = UserMessage.objects.create(
            owner = request.user.profile,
            room = room,
            body = request.POST.get('body'),
        )
        participant = request.user.profile
        room.participants.add(participant)
        return redirect('single_room',pk=room.id)
    context = {'room':room,'messages':messages,'participants':participants}
    return render(request,'base/single_room.html',context)


def activity_page(request):
    messages = UserMessage.objects.all()
    context = {'messages':messages}
    return render(request,'base/activity.html',context)

def topics_page(request):
    q = request.POST.get('q')
    topics = Topic.objects.all()
    if q is not None:
        topics = Topic.objects.filter(name__icontains=q)
    context = {'topics':topics}
    return render(request,'base/topics.html',context)
