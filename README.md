<b>1. Introduction</b> <br/>
This app accepts an input image (an image of a real estate property, exterior or interior) from user, and computes the feature tensor 
of the image using the VGG16 convolutional neural network up to the Conv-5 conv/max pooling layer (i.e., the last fully-connected and 
softmax prediction layers are removed). The output tensor is a sparse matrix having the dimension (7, 7, 512). This output tensor can be 
compared to ~ 700,000 property-image tensors stored in our databse for "similarity".

<b>2. Running the App</b> <br/>
To see the action of the app on the web, go to:  https://cnn-project-group3.herokuapp.com/index

<b>3. Jupyter Notebook</b> <br/>
If you are interested in the underlying algorithm for computing the similarity tensor, data conversion of the output tensor for efficient database storage, reconstructing the (7, 7, 512) tensor after extracting it from the database, and computing the "similarity score" between an input image and any given image in the database, please take a look at the jupyter notebook file provided in the repo: cnn_vgg16.ipynb <br/>
It is recommended that you run the IPython notebook under the Anaconda environment. Instructions for installing Anaconda and all necessary modules for Jupyter Notebook:
1. Download and Install Anaconda environment (this includes installing python 3.7): https://www.anaconda.com/ 

2. Current (as of August 2019) stable version of tensorflow does not support python 3.7, so we need to configure anaconda to run in python 3.6 environment, type in the anaconda terminal:<br/>
          >>> conda create -y --name tensorflow python=3.6

3. To enter tensorflow environment, type in the anaconda terminal (for Windows):>br/>
          >>> activate tensorflow <br/>
   (for OS, type: >>> source activate tensorflow)

4. Install Jupyter notebook: <br/>
          >>> conda install -y jupyter

5. To open jupyter notebook, type in the anaconda terminal: <br/>
          >>> jupyter notebook

6. Then in anaconda terminal, install the following modules needed for machine learning/deep learning: <br/>
          >>> conda install -y scipy <br/>
          >>> pip install --exists-action i --upgrade sklearn <br/>
          >>> pip install --exists-action i --upgrade pandas <br/>
          >>> pip install --exists-action i --upgrade pandas-datareader <br/>
          >>> pip install --exists-action i --upgrade matplotlib <br/>
          >>> pip install --exists-action i --upgrade pillow <br/>
          >>> pip install --exists-action i --upgrade tqdm <br/>
          >>> pip install --exists-action i --upgrade requests <br/>
          >>> pip install --exists-action i --upgrade h5py <br/>
          >>> pip install --exists-action i --upgrade pyyaml <br/>
          >>> pip install --exists-action i --upgrade tensorflow_hub <br/>
          >>> pip install --exists-action i --upgrade bayesian-optimization <br/>
          >>> pip install --exists-action i --upgrade spacy <br/>
          >>> pip install --exists-action i --upgrade gensim <br/>
          >>> pip install --exists-action i --upgrade flask <br/>
          >>> pip install --exists-action i --upgrade boto3 <br/>
          >>> pip install --exists-action i --upgrade gym <br/>
          >>> pip install --exists-action i --upgrade tf-nightly-2.0-preview <br/>
          >>> pip install --exists-action i --upgrade keras-rl2 --user <br/>
          >>> conda update -y --all

7. Finally, link tensorflow environment to jupyter so that we can run tensorflow under python 3.6; type in anaconda terminal: <br/>
          >>> python -m ipykernel install --user --name tensorflow --display-name "Python 3.6 (tensorflow)"

<b>4. Running the App Locally</b> </br>
If you are interested in seeing the app in action on your local machine, please do the following:
<ul>
  <li>Download the content of this repo by clicking the green "Clone or Download" button and select "Download ZIP"</li>
  <li>Unzip the content into a directory in your local machine</li>
  <li>Create a python virtual environment in this directory:</li>
    <ul>
      <li>In terminal, navigate to this directory, and type: >>> py -m venv env</li>
      <li>Activate this virtual environment by typing: >>> env\Scripts\activate</li>
      <li>Type: >>> pip install requirements.txt</li>
    </ul>
  <li>Run the app by typing (under the virtual env): >>> python routes.py</li>
</ul>
