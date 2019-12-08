from django.forms import ModelForm, Form

from video_gerenciador.models import Video
from django import forms


class Video_Form(forms.ModelForm):
    description = forms.CharField(required=False)
    artist = forms.CharField(required=False)
    director = forms.CharField(required=False)
    production_date = forms.DateField(required=False)

    class Meta:
        model = Video
        fields = ["title", "description", "artist", "director", "production_date"]
