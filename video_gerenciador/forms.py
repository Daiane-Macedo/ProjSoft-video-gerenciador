from django.forms import ModelForm, Form

from video_gerenciador.models import Video
from django import forms


class Video_Form(forms.ModelForm):
    YEARS = [x for x in range(1940, 2021)]

    description = forms.CharField(required=False)
    artist = forms.CharField(required=False)
    director = forms.CharField(required=False)
    production_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=YEARS))

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
