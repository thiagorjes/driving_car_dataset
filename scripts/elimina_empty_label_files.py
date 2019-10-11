import sys
import os
import cv2
from PIL import Image

def linecount(path):
    count = 0
    for line in open(path).xreadlines():
        count += 1
    return count

def principal(labels_path, images_path):
    total_ruim_img = 0
    total_ruim_lbl = 0
    for label_file in os.listdir(labels_path):
        try:
            f = open(labels_path + label_file, "r")
            img = Image.open(images_path + label_file.replace('txt', 'jpg'))
            img.verify()
            count = 0
            for line in f:
                if len(line) < 10:
                    continue
                count += 1
            if count == 0:
                total_ruim_lbl += 1
                os.remove(labels_path + label_file)
                print("removendo label defeituosa: " + labels_path + label_file+"\n")
            
        except:
            total_ruim_lbl += 1
            total_ruim_img += 1
            os.remove(labels_path + label_file)
            os.remove(images_path + label_file.replace('txt', 'jpg'))
            print("removendo imagem e label defeituosas: " + images_path + label_file.replace('txt', 'jpg')+"\n")

    print("total img:"+str(total_ruim_img))
    print("total lbl:"+str(total_ruim_lbl))

if len(sys.argv) == 3:
    if not sys.argv[1].endswith('/'):
        sys.argv[1] += '/'
    if not sys.argv[2].endswith('/'):
        sys.argv[2] += '/'

    principal(sys.argv[1], sys.argv[2])
else:
    print("\nusage: python "+sys.argv[0]+" labels/path/ images/path/ image_width image_heigth\n")

exit(0)