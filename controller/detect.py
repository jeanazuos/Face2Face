from model.detect import Detect

class DetectController:

    def __init__(self, request):
        self.request = request

    def check(self):
        return Detect(self.request).detect_faces()
