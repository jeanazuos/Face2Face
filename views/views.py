from flask import Blueprint, jsonify, request
from controller.validator import ValidatorController
from controller.detect import DetectController

my_bp = Blueprint('views', __name__)

@my_bp.route('/')
def index():
    return 'teste'

@my_bp.route('/api/check_faces', methods=['GET', 'POST'])
def upload_image():
    try:
        its_secure_files = ValidatorController(request).check()

        if its_secure_files:
            result = DetectController(its_secure_files).check()
            return jsonify(result), 200
        else: 
            result = {
                        "Error": "Invalid type, quantity or empty files",
                    }
            return jsonify(result), 400

    except Exception as e:
        print(f'Log error: {e}')
        result = {
                        "Error": "Internal Server Error", 
                    }
        return jsonify(result), 500
