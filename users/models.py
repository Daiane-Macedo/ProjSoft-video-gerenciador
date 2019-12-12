from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=255, null=False, verbose_name='Email')
    password = models.CharField(max_length=30, null=False, verbose_name='Senha')
    created_at = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name