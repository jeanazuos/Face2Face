import os
from flask import redirect, flash

def allowed_file(filename):
    ALLOWED_EXTENSIONS = os.getenv('ALLOWED_EXTENSIONS')
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_validator(request):
    try:
        checked_files = []
        # Check if a valid image file was uploaded
        if request.method == 'POST':
        
            if 'files[]' not in request.files:
                flash('No file part')
                return redirect(request.url)

            files = request.files.getlist('files[]')
  
            # Check if files has 2 images
            if len(files) != 2:
                return False

            for file in files:
                if file.filename == '':
                    return False

                if file and allowed_file(file.filename):
                    checked_files.append(file)
            return checked_files
    except Exception as e:
        print(e)
        return abort(400)