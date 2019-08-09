from tensorflow.keras.applications.vgg16 import VGG16
import re
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from models import db, User, Properties, Photos
from ast import literal_eval


# code to find closest match for input image
def closestMatches(input_img):

    # process the image and run it through the model (code from python notebook)
    img = load_img(input_img, target_size=(224, 224))
    image = img_to_array(img)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    
    # get the features
    vgg_model = VGG16(weights = 'imagenet', include_top = False)
    features = vgg_model.predict(image)


    # if we used places1365:
    # classification = FIND CLASSIFICATION WITH PLACES1365
    # all_photos = Photos.query.filter_by(classification=classification)

    # pull database set of all photos
    #all_photos = Photos.query.all()

    # for now, we are debugging using a smaller table
    all_photos = Photos.query.limit(100).all()

    # possible tracker variables to identify which cells to pop off the array
    mlsnums = []

    for photo in all_photos:
        # convert the stored string features into an array
        db_array = backToArr(literal_eval(photo.features))

        #compute the difference and append the set of values to the array
        difference = np.linalg.norm(db_array - features)
        mlsnums.append([photo.mlsnum, difference, photo.imgnum])

    
    
    # sort the array by the second column (distance) and then take fisrt 5 indices (this has been tested)
    sorted_array = sorted(mlsnums, key=lambda x: x[1]) 
    
    top_five = []
    match = False

    # loop to get distinct top 5 mlsnums
    for a in sorted_array:
        match = False
        if len(top_five) < 5:
            for b in top_five:
                if a[0] == b:
                    match = True
            if match == False:
                top_five.append(a[0])
        else:
            break

    return top_five



def backToArr(dict):
    arr = np.zeros((1, 7, 7, 512))

    for row in dict[0]:
        for col in dict[0][row]: 
            for elem in dict[0][row][col]:
                arr[0][row][col][elem] = dict[0][row][col][elem]
    return arr


