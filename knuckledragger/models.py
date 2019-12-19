from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# TODO Add Condition, Size, Faction FK
# TODO Finish Movie Ratings
# TODO Rewrite Racial Attributes as Tuple
# TODO Change description max length


#--------------(ALPHA)#--------------#
# TODO Fill in params in last_activity


DAY_CHOICES = [
    ('Sun', 'Sunday'),
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
]

MAX_PLAYERS = [
    (4, 'Four'),
    (5, 'Five'),
    (6, 'Six'),
]


RATING_CHOICES = [
    ('E', 'E')
]

# RACE_CHOICES = [
# 
# ]


class MailingList(models.Model):
    first_name = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)


class Item(models.Model):
    name = models.CharField(max_length=16)


class Character(models.Model):
    playable = models.BooleanField(default=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    max_health = models.PositiveSmallIntegerField(default=0)
    current_health = models.PositiveSmallIntegerField(default=0)
    weight = models.PositiveSmallIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    age = models.PositiveSmallIntegerField(default=0)
    authored_by = models.ForeignKey(User, on_delete=models.CASCADE)
    hussle = models.PositiveSmallIntegerField(default=0)

    # Equipment Slots + Inventory
    head = models.BooleanField(default=False)
    neck = models.BooleanField(default=False)
    shoulder = models.BooleanField(default=False)
    chest = models.BooleanField(default=False)
    left_arm = models.BooleanField(default=False)
    right_arm = models.BooleanField(default=False)
    left_hand = models.BooleanField(default=False)
    right_hand = models.BooleanField(default=False)
    belt = models.BooleanField(default=False)
    waist = models.BooleanField(default=False)
    left_leg = models.BooleanField(default=False)
    right_leg = models.BooleanField(default=False)
    left_foot = models.BooleanField(default=False)
    right_foot = models.BooleanField(default=False)
    accessory = models.BooleanField(default=False)
    wallet = models.IntegerField(default=0)

    # Attributes
    brawny = models.PositiveSmallIntegerField(default=0)
    sturdy = models.PositiveSmallIntegerField(default=0)
    speedy = models.PositiveSmallIntegerField(default=0)
    nerdy = models.PositiveSmallIntegerField(default=0)
    balky = models.PositiveSmallIntegerField(default=0)
    wily = models.PositiveSmallIntegerField(default=0)
    pritty = models.PositiveSmallIntegerField(default=0)
    gritty = models.PositiveSmallIntegerField(default=0)
    witty = models.PositiveSmallIntegerField(default=0)
    beastly = models.PositiveSmallIntegerField(default=0)
    techy = models.PositiveSmallIntegerField(default=0)
    outdoorsy = models.PositiveSmallIntegerField(default=0)

    # Skills
    hitting = models.PositiveSmallIntegerField(default=0)
    lifting = models.PositiveSmallIntegerField(default=0)
    brawny_special = models.PositiveSmallIntegerField(default=0)

    getting_hit = models.PositiveSmallIntegerField(default=0)
    not_dying = models.PositiveSmallIntegerField(default=0)
    sturdy_special = models.PositiveSmallIntegerField(default=0)

    finessing = models.PositiveSmallIntegerField(default=0)
    moving = models.PositiveSmallIntegerField(default=0)
    speedy_special = models.PositiveSmallIntegerField(default=0)

    analysis = models.PositiveSmallIntegerField(default=0)
    smarts = models.PositiveSmallIntegerField(default=0)
    nerdy_special = models.PositiveSmallIntegerField(default=0)

    tracking = models.PositiveSmallIntegerField(default=0)
    backbone = models.PositiveSmallIntegerField(default=0)
    balky_special = models.PositiveSmallIntegerField(default=0)

    stashing = models.PositiveSmallIntegerField(default=0)
    observing = models.PositiveSmallIntegerField(default=0)
    wily_special = models.PositiveSmallIntegerField(default=0)

    smooth_talking = models.PositiveSmallIntegerField(default=0)
    moxie = models.PositiveSmallIntegerField(default=0)
    pretty_special = models.PositiveSmallIntegerField(default=0)

    scaring = models.PositiveSmallIntegerField(default=0)
    leading = models.PositiveSmallIntegerField(default=0)
    gritty_special = models.PositiveSmallIntegerField(default=0)

    swindling = models.PositiveSmallIntegerField(default=0)
    blending = models.PositiveSmallIntegerField(default=0)
    witty_special = models.PositiveSmallIntegerField(default=0)

    taming = models.PositiveSmallIntegerField(default=0)
    tending = models.PositiveSmallIntegerField(default=0)
    beastly_special = models.PositiveSmallIntegerField(default=0)

    big_booms = models.PositiveSmallIntegerField(default=0)
    loud_vrooms = models.PositiveSmallIntegerField(default=0)
    techy_special = models.PositiveSmallIntegerField(default=0)

    scrouging = models.PositiveSmallIntegerField(default=0)
    guiding = models.PositiveSmallIntegerField(default=0)
    outdoorsy_special = models.PositiveSmallIntegerField(default=0)

    # Race
    arrivad = models.BooleanField(default=False)
    basahnin = models.BooleanField(default=False)
    ferrick = models.BooleanField(default=False)
    holeg = models.BooleanField(default=False)
    human = models.BooleanField(default=False)
    illawmi = models.BooleanField(default=False)
    kassari = models.BooleanField(default=False)
    khura = models.BooleanField(default=False)
    mogo = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class PlayerEquipment(models.Model):
    character_id = models.ForeignKey('Character', on_delete=models.CASCADE)


class Room(models.Model):
    # General Info
    room_name = models.CharField(max_length=16)
    authored_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    max_players = models.PositiveSmallIntegerField(default=4)
    rating = models.CharField(max_length=16)
    last_activity = models.DateField()
    
    # Schedule
    day = models.CharField(max_length=16, choices=DAY_CHOICES)
    time = models.TimeField()
    