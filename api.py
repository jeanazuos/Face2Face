import face_recognition
from flask import Flask, jsonify, request, redirect, flash

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
#It will allow below 16MB contents only, you can change it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    its_secure_files = []
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')
  
        for file in files:
            if file.filename == '':
                return redirect(request.url)

            if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
                its_secure_files.append(file)
    
    if len(its_secure_files) == 2:
        return detect_faces_in_image(its_secure_files)
    else:
    # If no valid image file was uploaded, show the file upload form:
        return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


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
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)