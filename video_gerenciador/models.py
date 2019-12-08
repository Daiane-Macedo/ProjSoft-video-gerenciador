
from django.db import models


# Create your models here.
from videoGerenciador.settings import MEDIA_ROOT


class Video(models.Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True, blank=True)
    artist = models.CharField(max_length=500, null=True, blank=True)
    director = models.CharField(max_length=500, null=True, blank=True)
    production_date = models.DateField(blank=True, null=True)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")

    class Meta:
        db_table = "video"

    def __str__(self):
        return str(self.file)
