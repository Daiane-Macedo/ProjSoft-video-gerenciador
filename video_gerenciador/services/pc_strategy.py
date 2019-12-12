from videoGerenciador.settings import VIDEO_URL

class PCUploadStrategy:
    @staticmethod
    def save(form, request):
        video = form.save(commit=False)
        video.file = request.FILES['video']
        video.save()
        videourl = (VIDEO_URL + str(video))
        video.file = videourl
        video.save()
        return video, videourl