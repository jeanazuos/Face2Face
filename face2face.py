'''
Construído baseado no exemplo da própria biblioteca face_recognition em:
ohttps://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py
'''

import face_recognition

# Load the jpg files into numpy arrays
main_image = face_recognition.load_image_file("TESTE_DE_BIOMETRIA_FACIAL/Item_47/Imagem_1.JPG")
compare_image = face_recognition.load_image_file("TESTE_DE_BIOMETRIA_FACIAL/Item_47/Imagem_2.JPG")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    main_face_encoding = face_recognition.face_encodings(main_image)[0]
    compare_face_encoding = face_recognition.face_encodings(compare_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    main_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, compare_face_encoding)

if results:
    if results[0] == True:
        print("Confere [✓]")
    else:
        print("Não confere [x]")
else:
    print("Não foi possível fazer a comparação de imagens")