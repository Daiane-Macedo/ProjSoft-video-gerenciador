# Create your views here.
from django.shortcuts import render

from videoGerenciador.settings import MEDIA_URL, MEDIA_ROOT, DEFAULT_FILE_STORAGE, AWS_S3_CUSTOM_DOMAIN, VIDEO_URL
from .forms import Video_Form
from .models import Video as videoModel
from django.views.generic import TemplateView


class Video(TemplateView):
    template_name = 'upload-form.html'

    def index_view(request):
        if request.method == 'GET':
            return render(request, 'index.html')

    def list_videos(request):
        if request.method == 'GET':
            videos = videoModel.objects.all().order_by('upload_date')
            return render(request, 'index.html', {'videos_list': videos})

    def show_video(request):
        if request.method == 'GET':
            form = Video_Form()
            context = {"form": form}
            return render(request, 'upload-form.html', context)

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
                return render(request, 'video.html', {'video': video, 'videourl': videourl})

        context = {"form": form}
        return render(request, 'upload-form.html', context)



