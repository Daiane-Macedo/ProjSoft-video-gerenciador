from django.forms import ModelForm, Form

from video_gerenciador.models import Video
from django import forms

class Youtube_Video_Form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "yt_url"]
        exclude = ['file']