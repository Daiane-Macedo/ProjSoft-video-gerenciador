from ..forms import Video_Form
from ..yt_forms import Youtube_Video_Form

class VideoFormFactory:
    @staticmethod
    def create(from_pc, request):
        if from_pc:
            return Video_Form(request.POST, request.FILES)
        else:
            return Youtube_Video_Form(request.POST)