from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from videoGerenciador import settings
from .models import Video
from .forms import VideoForm
from django.views.generic import TemplateView


class Video(TemplateView):
    template_name = 'index.html'

    def show_video(request):

        lastvideo = Video.objects.last()
        videofile = lastvideo.videofile

        form = VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context = {'videofile': videofile,
                   'form': form
                   }
        return render(request, '/index.html', context)

    def post_video(request):
        context = locals()
        if request.method == 'POST':
            form = VideoForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                form.save()

            return render(request, 'index.html', context)
