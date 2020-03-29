from PIL import Image
import face_recognition
from time import sleep

image =face_recognition.load_image_file('./img/groups/team2.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top,right,bottom, left = face_location

    fave_image = image[top:bottom,left:right]
    pil_image = Image.fromarray(fave_image)

    pil_image.save(f'{top}.jpg')