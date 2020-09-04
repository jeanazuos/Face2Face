import face_recognition

class Detect:
    def __init__(self, file_stream):
        self.file_stream = file_stream

    def detect_faces(self):
        # Load the uploaded image file
        image_one = face_recognition.load_image_file(self.file_stream[0])
        image_two = face_recognition.load_image_file(self.file_stream[1])

        # Get face encodings for any faces in the uploaded image
        face_encoding_one = face_recognition.face_encodings(image_one)
        face_encoding_two = face_recognition.face_encodings(image_two)

        face_found = False
        match_faces = False

        if len(face_encoding_one and face_encoding_two) > 0:
            face_found = True

            match_results = face_recognition.compare_faces(
                [face_encoding_one[0]], face_encoding_two[0])
            if match_results[0]:
                match_faces = True

        # Return the result as json
        result = {
            "face_found": face_found,
            "match_faces": match_faces
        }
        return result
