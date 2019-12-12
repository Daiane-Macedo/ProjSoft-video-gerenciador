# Create your views here.
import os

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from videoGerenciador.settings import VIDEO_URL
from video_gerenciador import utils
from .forms import Video_Form
from .models import Video as videoModel
from django.views.generic import TemplateView
from django.http import HttpRequest


class Video(TemplateView):
    template_name = 'upload-form.html'

    @require_http_methods(["GET"])
    def list_videos(request):
        videos = videoModel.objects.all().order_by('upload_date')

        return render(request, 'index.html', {'videos_list': videos})

    @require_http_methods(["GET"])
    def show_video(request):
        form = Video_Form()
        context = {"form": form}

        return render(request, 'upload-form.html', context)

    @require_http_methods(["GET", "POST"])
    def post_video(request):
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

    @require_http_methods(["POST"])
    def delete_video(request, id):
        newRequest = HttpRequest()
        newRequest.method = 'GET'
        # delete from s3 repository
        videoName = videoModel.objects.get(id=id).file
        path, filename = os.path.split(videoName.name)
        utils.delete_from_S3(filename)
        # delete from db
        videoModel.objects.filter(id=id).delete()

        return redirect('/')

    @require_http_methods(["POST"])
    def edit_video(request, id):
        form = Video_Form()
        context = {"form": form, 'id': id}
        return render(request, 'edit.html', context)

    @require_http_methods(["POST"])
    def update_video(request, id):
        instance = get_object_or_404(videoModel, id=id)
        form = Video_Form(request.POST, instance=instance)
        context = {'form': form}

        if form.is_valid():
            form.id = id
            video = form.save(commit=False)
            video.save(update_fields=["title", "description", "artist", "director", "production_date"])
            context = {'form': form}
            return redirect('/')
        else:
            context = {'form': form,
                       'id': id,
                       'error': 'Erro ao editar o formulário'}

            return render(request, 'edit.html', context)

