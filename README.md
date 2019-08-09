1. Introduction <br/>
This app accepts an input image (an image of a real estate property, exterior or interior) from user, and computes the feature tensor 
of the image using the VGG16 convolutional neural network up to the Conv-5 conv/max pooling layer (i.e., the last fully-connected and 
softmax prediction layers are removed). The output tensor is a sparse matrix with dimension (7, 7, 512). This output tensor can be 
compared to ~ 700,000 property-image tensors stored in our databse for "similarity". 
