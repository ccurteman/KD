from django import forms
from .models import Room

# Create the form class for rooms
class RoomForm(forms.Form):
    room_name = forms.CharField(max_length=16)
    description = forms.CharField(max_length=200)
    max_players = forms.IntegerField(max_value=6, min_value=4)