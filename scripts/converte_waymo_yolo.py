import matplotlib.patches as patches
import matplotlib.pyplot as plt
import enum
from waymo_open_dataset import dataset_pb2 as open_dataset
from waymo_open_dataset.utils import frame_utils
from waymo_open_dataset.utils import transform_utils
from waymo_open_dataset.utils import range_image_utils
import os
import tensorflow as tf
import math
import numpy as np
import itertools
import glob

tf.enable_eager_execution()


# read frames from dataset
DATASET_PATH= '/WAYMO/parte1/'
IMAGES_OUT_PATH='/YOLO/imagens/'
LABELS_OUT_PATH='WAYMO/parte1/' #'/YOLO/labels/'

def SaveFrameImageAndLabels(camera_image, myframe,indice):
    # get image data to retrieve width and height
    temp =tf.image.decode_jpeg(camera_image.image)
    width = temp.shape[1]
    height = temp.shape[0]
    #create labels file
    text_file = open(LABELS_OUT_PATH+(['UNKNOWN','FRONT','FRONT_LEFT','FRONT_RIGHT','SIDE_LEFT','SIDE_RIGHT'][camera_image.name])+"_"+indice+".txt", "w")
    #save image
    #not done yet

    # Draw the camera labels.
    for camera_labels in myframe.camera_labels:
        # Ignore camera labels that do not correspond to this camera.
        if camera_labels.name != camera_image.name:
            continue
        # Iterate over the individual labels.
        for label in camera_labels.labels:
            # create label line
            # ['UNKNOWN',  'VEHICLE',  'PEDESTRIAN',  'SIGN', 'CYCLIST'][label.type]
            # classID center_x center_y relative_width relative_height
            text_file.write(str(label.type)+" "+str(float(label.box.center_x/int(width)))+" "+str(float(label.box.center_y/int(height)))+" "+str(float(label.box.length/int(width)))+" "+str(float(label.box.width/int(height))))
    text_file.close()

#find files tfrecord to open
def IterateFiles(path):
    files = [f for f in glob.glob(path + "**/*.tfrecord", recursive=True)]
    arquivo_idx=0
    for f in files:
        dataset = tf.data.TFRecordDataset(f, compression_type='')
        # print(f)
        # for each tfrecord get images and labels
        indice = 0
        for data in dataset:            
            frame = open_dataset.Frame()        
            frame.ParseFromString(bytearray(data.numpy()))
            #(range_images, camera_projections,range_image_top_pose) = frame_utils.parse_range_image_and_camera_projection(frame)
            sufixo = str(arquivo_idx)+"_"+str(indice)
            SaveFrameImageAndLabels(frame.images[0],frame,sufixo)
            SaveFrameImageAndLabels(frame.images[1],frame,sufixo)
            SaveFrameImageAndLabels(frame.images[2],frame,sufixo)
            SaveFrameImageAndLabels(frame.images[3],frame,sufixo)
            SaveFrameImageAndLabels(frame.images[4],frame,sufixo)
            indice += 1
        arquivo_idx += 1

IterateFiles(DATASET_PATH)
print("fim")