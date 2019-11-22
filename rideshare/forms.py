from django import forms

from .models import Profile, requests, offer
import datetime

def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value



class RequestForm(forms.ModelForm):
    depart_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'form-control'}), validators=[present_or_future_date])
    depart_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time', 'class':'form-control'}))
    desired_price = forms.IntegerField(min_value=1, widget=forms.widgets.NumberInput(attrs={'class':'form-control'}))
    start_location = forms.CharField(widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    end_location = forms.CharField(widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    notes = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'form-control', 'rows': '3'}), required=False)
    class Meta:
        model = requests
        fields = ('start_location', 'end_location', 'depart_date', 'depart_time', 'desired_price', 'notes')

class OfferForm(forms.ModelForm):
    depart_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'form-control'}), validators=[present_or_future_date])
    depart_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type':'time', 'class':'form-control'}))
    price = forms.IntegerField(min_value=1, widget=forms.widgets.NumberInput(attrs={'class':'form-control'}))
    seats = forms.IntegerField(min_value=1,widget=forms.widgets.NumberInput(attrs={'class':'form-control'}))
    start_location = forms.CharField(widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    end_location = forms.CharField(widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    notes = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'form-control', 'rows': '3'}), required=False)
    class Meta:
        model = offer
        fields = ('start_location', 'end_location', 'depart_date', 'depart_time', 'price', 'seats', 'notes')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('hometown', 'car', 'phone_number', 'preferred_payment')
