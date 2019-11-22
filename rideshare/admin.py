from django.contrib import admin

# Register your models here.
from .models import requests, offer, Profile, SignUp



admin.site.register(requests)
admin.site.register(offer)
admin.site.register(Profile)
admin.site.register(SignUp)

