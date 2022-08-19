import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from tensorflow.keras.models import load_model
import sys
import time
import numpy as np

import airsim

import keras.backend as K
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Connect to AirSim 
client = airsim.CarClient()
client.confirmConnection()
car_controls = airsim.CarControls()

position = client.simGetObjectPose("car1").position
print("Starting coordinates")
print("x")
print(position.x_val)
print("y")
print(position.y_val)


while True:    

    # Print progress
    #print('Sending steering = {0}, throttle = {1}, prediction time = {2}'.format(received_output, car_controls.throttle,str(end_time-start_time)))
    position = client.simGetObjectPose("car1").position
    print("x_val")
    print(position.x_val)
    print("y_val")
    print(position.y_val)
