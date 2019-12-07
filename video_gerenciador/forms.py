from django.forms import ModelForm, Form

from video_gerenciador.models import Video
from django import forms


class Video_Form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "description"]
