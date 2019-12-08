from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
	User = models.OneToOneField(
        User,
		default=None,
		null=True,
        on_delete=models.CASCADE,
    )
	phone_number = models.CharField(max_length=10, default=None, null=True)
	birthday = models.CharField(max_length=20, default=None)

class person(models.Model):
	name_choices = (
	('Adam', "Adam"),
	('Jack', "Jack"),
	('Reid', "Reid"),
	('Ryan', "Ryan"),
	('Trevor', "Trevor"),
	('Will', "Will"),
	('William', "William"))
	name = models.CharField(max_length=8,
                  choices=name_choices,
                  default= 1)
	queue = models.IntegerField(default=None, null=True)
	notes = models.CharField(max_length=200, default=None,null=True)

class room(models.Model):
	notes = models.CharField(max_length=200, default=None,null=True)
	room_choices = (
	("Adam's Current Room", "Adam's Current Room"),
	("Mike's Current Room", "Mike's Current Room"),
	("Jeremy's Current Room", "Jeremy's Current Room"),
	("Ryan's Current Room", "Ryan's Current Room"),
	("Trevor's Current Room", "Trevor's Current Room"),
	("Will's Current Room", "Will's Current Room"),
	("Owen's Current Room", "Owen's Current Room"))
	room_choice = models.CharField(max_length=30,
                  choices=room_choices,
                  default= 1)
	selected = models.IntegerField(default=0, null=True)
	original = models.IntegerField(default=0, null=True)
