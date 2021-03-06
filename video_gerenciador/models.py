from django.db import models
from django.utils import timezone
# Create your models here.


class Video(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True, blank=True)
    artist = models.CharField(max_length=500, null=True, blank=True)
    director = models.CharField(max_length=500, null=True, blank=True)
    production_date = models.DateField(blank=True, null=True)
    file = models.FileField(null=True, verbose_name="")
    upload_date = models.DateTimeField(editable=False)
    yt_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="URL do YT")
    image = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = "video"

    def __str__(self):
        self.upload_date = timezone.now()
        return str(self.file)
