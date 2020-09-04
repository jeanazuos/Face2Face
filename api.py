import os
from validation_files import file_validator
from flask import Flask, jsonify, request
from model.detect import Detect

app = Flask(__name__)

# Limit file size
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH'))

@app.route('/api/check_faces', methods=['GET', 'POST'])
def upload_image():
    try:
        its_secure_files = file_validator(request)
        print(its_secure_files)
        # If dont have files returns will be False
        if its_secure_files:
            result = Detect(its_secure_files).detect_faces()
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)