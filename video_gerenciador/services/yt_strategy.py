from urllib.parse import urlparse
from urllib.parse import parse_qs

class YTUploadStrategy:
    @staticmethod
    def save(form, request):
        video = form.save(commit=False)
        video.title = request.POST['title']
        video.yt_url = request.POST['yt_url']
        video.image = YTUploadStrategy.get_image(video.yt_url)
        video.save()
        return video, video.yt_url

    @staticmethod
    def get_image(yt_url):
        url_data = urlparse(yt_url)
        query = parse_qs(url_data.query)
        id = query["v"][0]
        return "http://img.youtube.com/vi/"+id+"/maxresdefault.jpg"