import sys
import os
import cv2


def linecount(path):
    count = 0
    for line in open(path).xreadlines():
        count += 1
    return count


def main(labels_path, images_path):
    for label_file in os.listdir(labels_path):
        try:
            f = open(labels_path + label_file, "r")
            print(images_path + label_file.replace('txt', 'jpg'))
            img = cv2.imread(images_path + label_file.replace('txt', 'jpg'))

            image_dimensions = [img.shape[1],img.shape[0]]
            count = 0
            for line in f:
                if len(line) < 10:
                    continue
                count += 1
                box = line.strip().split()
                x1 = int((float(box[1]) - (float(box[3]) / 2)) * image_dimensions[0])
                y1 = int((float(box[2]) - (float(box[4]) / 2)) * image_dimensions[1])
                x2 = int((float(box[1]) + (float(box[3]) / 2)) * image_dimensions[0])
                y2 = int((float(box[2]) + (float(box[4]) / 2)) * image_dimensions[1])
                print( str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2))
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

            while (1):
                cv2.imshow('Yolo View', img)
                key = cv2.waitKey(0) & 0xff
                print(key)
                if key == 10:      # Enter key
                    print("enter pressionado")
                    break
                elif key == 27:    # ESC key
                    print("esc pressionado")
                    return
        except Exception as ex:
            print("deu ruim:"+ex)


if len(sys.argv) == 3:
    if not sys.argv[1].endswith('/'):
        sys.argv[1] += '/'
    if not sys.argv[2].endswith('/'):
        sys.argv[2] += '/'

    main(sys.argv[1], sys.argv[2])
else:
    print("\nusage: python " +
          sys.argv[0]+" labels/path/ images/path/ image_width image_heigth -format jpg\n")
