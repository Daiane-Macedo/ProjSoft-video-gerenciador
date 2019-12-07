
from django.db import models


# Create your models here.
from videoGerenciador.settings import MEDIA_ROOT


class Video(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    content = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return str(self.content)
