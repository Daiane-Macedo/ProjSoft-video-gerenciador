class YTUploadStrategy:
    @staticmethod
    def save(form, request):
        video = form.save(commit=False)
        video.title = request.POST['title']
        video.yt_url = request.POST['yt_url']
        video.save()
        return video, video.yt_url