from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from videoGerenciador import settings
from .views import Video

app_name = "app"

urlpatterns = [
                path('', Video.as_view(), name='index_view'),
                path('video', Video.post_video, name='video')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
