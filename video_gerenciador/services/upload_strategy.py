from .pc_strategy import PCUploadStrategy
from .yt_strategy import YTUploadStrategy

class UploadStrategy:
    @staticmethod
    def save(from_pc, form, request):
        if from_pc:
            return PCUploadStrategy.save(form, request)
        else:
            return YTUploadStrategy.save(form, request)