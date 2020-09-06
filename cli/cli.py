'''
Construído baseado no exemplo da própria biblioteca face_recognition em:
https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py
'''

import face_recognition
import os

# To be continue or finish the while execute
def try_new_test():
    execute = input("\nGostaria de fazer um novo teste?\nDigite 1 para SIM ou 0 para NAO:\n")
    if execute == '1':
        execute = True
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        execute = False
        print("\n---FIM---")
        quit()
    return execute

# Run menu
execute = True
while execute == True:
    print("\n------ TESTE DE BIOMETRIA FACIAL ------\n")

    # Set the config path and name files
    main_path = os.getenv("CLI_MAIN_PATH_CHECK", "TESTE_DE_BIOMETRIA_FACIAL")
    image_path = input("Insira o nome da pasta a ser analisado EX: 'Item_7':\n")
    image_name_one = os.getenv("CLI_DEFAULT_IMAGE_NAME_ONE", "Imagem_1.JPG")
    image_name_two = os.getenv("CLI_DEFAULT_IMAGE_NAME_ONE", "Imagem_2.JPG")

    # Load the jpg files into numpy arrays
    try:
        main_image = face_recognition.load_image_file(main_path + "/" + image_path + "/" + image_name_one)
        compare_image = face_recognition.load_image_file(main_path + "/" + image_path + "/" + image_name_two)
    except Exception as e:
        print("\nPasta nao existe ou possui algum problema de caracter.")
        print(e)
        try_new_test()
        continue

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
            print(f"\nPasta: {image_path}\nResultado: Confere [✓]\nDiretorio: {'/'+ main_path + '/' +image_path }\n---------------------------------------------------")
            
        else:
            print(f"\nPasta: {image_path}\nResultado: Nao confere [x]\nDiretorio: {'/'+ main_path + '/' +image_path }\n---------------------------------------------------")
    else:
        print("Não foi possível realizar a comparação de imagens")
    
    try_new_test()
