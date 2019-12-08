from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from videoGerenciador import settings
from videoGerenciador.settings import MEDIA_URL, MEDIA_ROOT
from .models import Video
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
                return render(request, 'upload.html', {'video': video})

        context = {"form": form}
        return render(request, 'upload.html', context)