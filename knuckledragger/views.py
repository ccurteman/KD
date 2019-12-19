import requests, os
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Character, Room

from .actions import MeleeAttack
from .forms import RoomForm


def landing(request):
    return render(request, 'site/landing.html')

# TODO Add Filtering Options to lobby (probably need to queryset in view)
class lobby(ListView):
    model = Room
    template_name = 'site/lobby.html'
    context_object_name = 'rooms'
    ordering = ['-date_created']


class room(ListView):
    model = Room
    template_name = 'site/room.html'
    text_object_name = 'room'


@login_required
def create_item(request):
    return render(request, 'create/item.html')


@login_required
def create_npc(request):
    return render(request, 'create/npc.html')


@login_required
def create_pc(request):
    return render(request, 'create/pc.html')


@login_required
def create(request):
    return render(request, 'create/create.html')

# TODO Delete me

# FUNCTIONS FOR ROOM #
from .actions import MeleeAttack

def get_melee_attack(request):
    # if this is a POST request we need to process the melee attack data
    if request.method == 'POST':
        # create a melee attack instance and populate it with data from the request:
        melee_attack = MeleeAttack(request.POST)
        # check whether it's valid:
        if melee_attack.is_valid():
            # process the data in melee attack.cleaned_data as required
            
            # get all the info

            # run the equation

            # make a database POST to update with new info
            return

    # if a GET (or any other method) we'll create a blank melee attack
    else:
        melee_attack = MeleeAttack()

    return render(request, 'room.html', {'melee attack': melee_attack})


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['room_name']
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            day = form.cleaned_data['day']
            room = Room(room_name=name, desciption=description, rating=rating, day=day, date_created=datetime.now(), authored_by=User.username)
            room.save()
            # redirect to a new URL:
            return render(request, 'room.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        room_form = RoomForm()

    return render(request, 'room.html', {'room_form': room_form})