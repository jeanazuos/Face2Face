def allowed_file(filename):
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
  
            for file in files:
                if file.filename == '':
                    return redirect(request.url)

                if file and allowed_file(file.filename):
                    checked_files.append(file)
            print(checked_files)
            return checked_files
    except Exception as e:
        print(e)