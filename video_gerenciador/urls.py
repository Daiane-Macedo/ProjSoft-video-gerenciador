from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from videoGerenciador import settings
from .views import Video

app_name = "app"

urlpatterns = [
                path('video', Video.show_video, name='video'),
                path('upload', Video.post_video, name='upload'),
                path('upload_youtube', Video.new_video_youtube, name='upload_youtube'),
                path('new_video', Video.new_video, name='new_video'),
                path('', Video.list_videos, name='home'),
                path('admin/', admin.site.urls),
                url(r'^update/(?P<id>[0-9]+)/$', Video.update_video, name='update'),
                url(r'^edit/(?P<id>[0-9]+)/$', Video.edit_video, name='edit'),
                url(r'^delete/(?P<id>[0-9]+)/$', Video.delete_video, name='delete'),
                path('', include('users.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
