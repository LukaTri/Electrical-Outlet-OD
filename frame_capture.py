import cv2
import os
import uuid
import time

# Specify the number of images to be collected duing one run of the code
num_images = 5

# Creating the different outlet labels
labels = ['unused', 'used']
IMAGES_PATH = os.path.join(os.getcwd(), 'collected_images', 'test_images')
print(f"image path directory {IMAGES_PATH}")

# Create a file path for each label we want to create; will work for MacOS/Linux and Windows
if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
        os.makedirs(IMAGES_PATH)
    if os.name == 'nt':
         os.makedirs(IMAGES_PATH)

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)

# Press the Space Bar when the console is printing 'Collecting image _'. To quit the program, press the escape key at any point.
# Code adopted from this StackOverflow post:
# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
cam = cv2.VideoCapture(2)
cv2.namedWindow("test")
flag = False
for label in labels:
    img_counter = 0
    print('Collecting images for {}'.format(label))
    while(img_counter < num_images):
        ret, frame = cam.read()
        if not ret:
            print('Failed to grab frame')
            flag = True
            break
        cv2.imshow('test', frame)
        print('Collecting image {}'.format(img_counter))
        k = cv2.waitKey(1)
        if k%256 == 27:
            print('Escape hit, closing...')
            flag = True
            img_counter = 999
            break
        elif k%256 == 32:
            img_name = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(img_name, frame)
            print('{} written!'.format(img_name))
            img_counter += 1
    if flag:
        break

cam.release()
cv2.destroyAllWindows()