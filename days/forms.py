from django import forms

from .models import Profile, person, room
import datetime


class PersonForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'form-control', 'rows': '3', 'placeholder':'To verify your identity, put something that only I would know'}), required=True)
    class Meta:
        model = person
        fields = ('name', 'notes')


class RoomForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'form-control', 'rows': '3', 'placeholder':'Why do you want this room?'}), required=True)
    class Meta:
        model = room
        fields = ('room_choice', 'notes')


class RoomTwoForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.widgets.Textarea(attrs={'class':'form-control', 'rows': '3', 'placeholder':'Why do you want this room?'}), required=False)
    selected = forms.IntegerField(min_value=0, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'value':0}))
    original = forms.IntegerField(min_value=0, widget=forms.widgets.NumberInput(attrs={'class':'form-control', 'value':1}))
    class Meta:
        model = room
        fields = ('room_choice', 'notes','selected','original')
