from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from videoGerenciador import settings
from .views import Video

app_name = "app"

urlpatterns = [
                path('', Video.index_view, name='index_view'),
                path('upload', Video.show_video, name='upload'),
                path('video', Video.post_video, name='video')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
