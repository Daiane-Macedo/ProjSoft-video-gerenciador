from django.forms import ModelForm, Form

from video_gerenciador.models import Video
from django import forms


class Video_Form(forms.ModelForm):

    description = forms.CharField(required=False)
    artist = forms.CharField(required=False)
    director = forms.CharField(required=False)
    production_date = forms.DateField(required=False, input_formats=['%d-%m-%Y'], label=None,)

    class Meta:
        model = Video
        fields = ["title", "description", "artist", "director", "production_date"]

    def __init__(self, *args, **kwargs):
        super(Video_Form, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Título"
        self.fields['description'].label = "Descrição"
        self.fields['artist'].label = "Artista"
        self.fields['director'].label = "Diretor"
        self.fields['production_date'].label = "Data de produção"
        self.fields['production_date'].widget.attrs['placeholder'] = '00-00-0000'
