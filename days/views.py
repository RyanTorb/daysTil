from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
from .models import Profile, room, person
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .forms import PersonForm, RoomForm, RoomTwoForm
import datetime

order = ['Will','Adam','Trevor','Ryan','Jack','William','Reid']

#@login_required(login_url='..')
def temp(request, n):
    os = room.objects.all().filter(original=1)
    sum = 7 - len(os)
    position = 'Unknown'
    for i in range(len(order)):
        if order[i]==n:
            position = i
    position = position - sum
    context = {
        'name' : n,
        'position' : position+1,
        'sum': len(os)
    }
    return render(request, 'days/interim.html', context)

def index(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        prof = form.save(commit=False)
        form.save()
        form = PersonForm()
        return temp(request, prof.name)
    return render(request, "days/new_profile.html", {'form' : form} )

def LoginView(request):
    template = loader.get_template('days/login.html')
    return HttpResponse(template.render({}, request))

def Select(request):
    os = room.objects.all().filter(original=1)
    context = {
        'ops': os
    }
    return render(request, 'days/select_room.html', context)

def end(request):
    template = loader.get_template('days/end.html')
    return HttpResponse(template.render({}, request))

def add(request):
    form = RoomTwoForm(request.POST or None)
    if form.is_valid():
        prof = form.save(commit=False)
        form.save()
        form = RoomTwoForm()
        return LoginView(request)
    return render(request, "days/select_room2.html", {'form' : form} )

def delete(request, key):
    post = room.objects.get(pk=key)
    post.delete()
    return end(request)