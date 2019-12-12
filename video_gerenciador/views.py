# Create your views here.
import os

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from videoGerenciador.settings import MEDIA_URL, MEDIA_ROOT, DEFAULT_FILE_STORAGE, AWS_S3_CUSTOM_DOMAIN, VIDEO_URL
from video_gerenciador import utils
from .forms import Video_Form
from .models import Video as videoModel
from django.views.generic import TemplateView
from django.http import HttpRequest


class Video(TemplateView):
    template_name = 'upload-form.html'

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

    def delete_video(request, id):
        newRequest = HttpRequest()
        newRequest.method = 'GET'

        if request.method == 'POST':
            # delete from s3 repository
            videoName = videoModel.objects.get(id=id).file
            path, filename = os.path.split(videoName.name)
            utils.delete_from_S3(filename)
            # delete from db
            videoModel.objects.filter(id=id).delete()

        return redirect('/')

    def edit_video(request, id):
        form = Video_Form()
        context = {"form": form, 'id': id}
        print(context)
        return render(request, 'edit.html', context)

    def update_video(request, id):

        if request.method == 'POST':
            print(id)
            instance = get_object_or_404(videoModel, id=id)
            form = Video_Form(request.POST, instance = instance)
            context = {'form': form}
            print(form.is_valid())
            if form.is_valid():
                form.id = id
                video = form.save(commit=False)
                video.save(update_fields=["title", "description", "artist", "director", "production_date"])
                messages.success(request, "Vídeo atualizado com sucesso")
                context = {'form': form}
                return redirect('/')

            else:
                context = {'form': form,
                           'id':id,
                           'error': 'Erro ao editar o formulário'}
                return render(request, 'edit.html', context)

