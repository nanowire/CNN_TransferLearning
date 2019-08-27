<b>1. Introduction</b> <br/>
This app accepts an input image (an image of a real estate property, exterior or interior) from user, and computes the feature tensor 
of the image using the VGG16 convolutional neural network up to the Conv-5 conv/max pooling layer (i.e., the last fully-connected and 
softmax prediction layers are removed). The output tensor is a sparse matrix having the dimension (7, 7, 512). This output tensor can be 
compared to ~ 700,000 property-image tensors stored in our databse for "similarity".

<b>2. Jupyter Notebook</b>
If you are interested in the underlying algorithm for computing the similarity tensor, data conversion of the output tensor for efficient database storage, reconstructing the (7, 7, 512) tensor after extracting it from the database, and computing the "similarity score" between an input image and any given image in the database, please take a look at the jupyter notebook file provided in the repo: cnn_vgg16.ipynb

<b>3. Running the App Locally</b>
If you are interested in seeing the app in action on your local machine, please do the following:
<ul>
  <li>Download the content of this repo by clicking the green "Clone or Download" button and select "Download ZIP"</li>
  <li>Unzip the content into a directory in your local machine</li>
  <li>Create a virtual environment in this directory:</li>
  <ul>
    <li>a</li>
  </ul>
</ul>
