import os
import glob
known_faces = []
known_names = []
known_faces_paths = []

registered_faces_path = 'registered/'
for name in os.listdir(registered_faces_path):
    images_mask = '%s%s/*.jpg' % (registered_faces_path, name)
    images_paths = glob.glob(images_mask)
    known_faces_paths += images_paths
    known_names += [name for x in images_paths]
for name,images_path in zip(known_names, known_faces_paths):
    print('%s: %s' % (name, images_path))
import face_recognition
def get_encodings(img_path):
    image = face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(image)
    return encoding[0]
known_faces = [get_encodings(img_path) for img_path in known_faces_paths]
unknown_images = glob.glob('unknown/*.jpg')
import matplotlib.pyplot as plt

for img_path in unknown_images:
    img = plt.imread(img_path)
    plt.figure()
    plt.imshow(img)
    encodings = face_recognition.face_encodings(img)
    found_faces = []
    for face_code in encodings:
        results = face_recognition.compare_faces(known_faces, face_code, tolerance=0.6)
        if any(results):
            found_faces.append(known_names[results.index(True)])

    plt.title('In the image: %s ' % str(found_faces))
