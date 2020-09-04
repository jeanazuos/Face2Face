from model.validation_files import Validation

class ValidatorController:

    def __init__(self, request):
        self.request = request
    
    def check(self):
        return Validation(self.request).file_validator()
