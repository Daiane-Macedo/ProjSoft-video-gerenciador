# Create your views here.
from django.shortcuts import render

from videoGerenciador.settings import MEDIA_URL, MEDIA_ROOT, DEFAULT_FILE_STORAGE, AWS_S3_CUSTOM_DOMAIN, VIDEO_URL
from .forms import Video_Form
from django.views.generic import TemplateView


class Video(TemplateView):
    template_name = 'upload.html'

    def index_view(request):
        return render(request, 'index.html')

    def show_video(request):
        if request.method == 'GET':
            form = Video_Form()
            context = {"form": form}
            return render(request, 'upload.html', context)

    def post_video(request):
        form = Video_Form()
        if request.method == 'POST':
            form = Video_Form(request.POST, request.FILES)
            if form.is_valid():
                video = form.save(commit=False)
                video.file = request.FILES['video']
                video.save()
                videourl = (VIDEO_URL + str(video))
                video.file = videourl
                video.save()
                return render(request, 'upload.html', {'video': video, 'videourl': videourl})

        context = {"form": form}
        return render(request, 'upload.html', context)



