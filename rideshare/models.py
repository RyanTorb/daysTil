from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
import datetime

class requests(models.Model):
	start_location = models.CharField(max_length=200)
	end_location = models.CharField(max_length=200)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(
			User,
			on_delete=models.CASCADE,
			default=None,
			null=True,
	)	
	depart_date = models.DateField()
	depart_time = models.TimeField()
	desired_price = models.IntegerField(default=None, null=True)
	notes = models.CharField(max_length=200, default=None, null=True)


class offer(models.Model):
	start_location = models.CharField(max_length=200, default=None, null=True)
	end_location = models.CharField(max_length=200, default=None, null=True)
	date_posted = models.DateTimeField(default=timezone.now, null=True)
	author = models.ForeignKey(
			User,
			on_delete=models.CASCADE,
			default=None,
			null=True,

	)	
	depart_date = models.DateField(default=None, null=True)
	depart_time = models.TimeField(default=None, null=True)
	price = models.IntegerField(default=None, null=True)
	seats = models.IntegerField(default=None, null=True)
	notes = models.CharField(max_length=200, default=None,null=True)
	seats_open = models.IntegerField(default=None, null=True)

	
class SignUp(models.Model):
	offer = models.ForeignKey(offer, on_delete=models.CASCADE)
	user = models.ForeignKey(
			User, 
			on_delete=models.CASCADE,
			default=None,
			null=True,
	)

class Profile(models.Model):
	User = models.OneToOneField(
        User,
		default=None,
		null=True,
        on_delete=models.CASCADE,
    )
	phone_number = models.CharField(max_length=10, default=None, null=True)
	car = models.CharField(max_length = 200)
	hometown = models.CharField(max_length = 200)
	PAYMENT_CHOICES = (
	('Venmo', "Venmo"),
	('Cashapp', "Cashapp"),
	('Cash', "Cash"),
	('Paypal', "Paypal"),
	('Check', "Check"),
	('Other', "Other"))
	preferred_payment = models.CharField(max_length=7,
                  choices=PAYMENT_CHOICES,
                  default= 1)
	
	

# @receiver(post_save, sender=user)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=user)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
