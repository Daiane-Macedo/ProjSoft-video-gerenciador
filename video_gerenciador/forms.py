from django.forms import ModelForm, Form

from video_gerenciador.models import Video
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "videofile"]
