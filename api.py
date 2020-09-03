import face_recognition
import os
from validation_files import file_validator
from flask import Flask, jsonify, request

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
            result = detect_faces_in_image(its_secure_files)
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



    


def detect_faces_in_image(file_stream):

    # Load the uploaded image file
    img1 = face_recognition.load_image_file(file_stream[0])
    img2 = face_recognition.load_image_file(file_stream[1])
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img1)
    unknown_face_encodings2 = face_recognition.face_encodings(img2)



    face_found = False
    is_obama = False

    if len(unknown_face_encodings and unknown_face_encodings2) > 0:
        face_found = True
        # See if the first face in the uploaded image matches the known face of Obama
        match_results = face_recognition.compare_faces([unknown_face_encodings[0]], unknown_face_encodings2[0])
        if match_results[0]:
            is_obama = True

    # Return the result as json
    result = {
        "face_found_in_image": face_found,
        "is_picture_of_obama": is_obama
    }
    return result

    '''
    INCLUIR OUTROS RETORNOS
    CRIAR UM CHECK PARA CASO NAO TENHA ENCONTRADO ROSTOS RETORNAR ALGUM ERRO
200
400
404
408
500
'''
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)