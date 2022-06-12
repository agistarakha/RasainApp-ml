# RASAIN (Indonesian food Image classification)
Indonesian food Image classification using TensorFlow.

# Information:
## Data Preparation
Contains all files required for data preparation (Image Data Gathering, Resizing Image)
## Model History
Contain output for model train history in pdf format and other model in unused folder
## Model Project
Model used for image classification
## Saved Model
Contain ready to deploy model

# Related Project Repository
|Links|Description|
|-----|-----------|
|https://github.com/ChristanFarel/RasainApp|Android Project|
|https://github.com/andikabahari/RasainApp-backend|Cloud Computing Project|

# Documentation
## Data Preparation Process
### Data Gathering
We gathered the dataset manually from google image  
#### Data Gathering Process:  
- Request google image search query using SERP API to get an unique image url.
- Loop through the list of saved urls and download images from the url.
- Remove dataset noise (Remove image that does not represent its class)  
#### There are 10 Classes that we used:  
- Bakso
- Rendang
- Sate
- Klepon
- Pastel
- Tumpeng
- Nastar
- Onde-onde
- Nasi goreng
- Tahu Petis  
Each class consists of 416 images for the train set and 100 images for the test set.  
### Data Processing
Before we use the image dataset to create the model, each image will be resized to 150x150 with padding, to prevent image distortion. Then we augment the image dataset by rescaling, rotating, flipping and adding labels on each image in the dataset.  
### Model Creation
We use 3 layers of CNN with ten outputs based on the food class in the dataset. then the model will be compiled using:  
- optimizers Adam (lr = 0.001)
- loss = categorical crossentropy
## How to use
### Requirements
- Node.js v16
- Tensorflow for python
- Tensorflow JS library for Node JS
- Image Processing Library for python and javascript  
### Download Model
Download one of the models that located in: https://github.com/agistarakha/RasainApp-ml/tree/main/Saved%20Model
### Prediction
#### Python
```python
img = image.load_img($IMAGE_PATH, target_size=(150, 150)) # Load image and resize the image
x = image.img_to_array(img) # Convert image to array
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(classes)
  ```
#### Node JS
```javascript
const tf = require("@tensorflow/tfjs-node");

const predict = async (image) => {
  image = tf.node.decodeImage(image);
  image = tf.expandDims(image);
  const path = `$MODEL_PATH`;
  const model = await tf.loadLayersModel(path);
  const result = model.predict(image);
  return result.data();
};

module.exports = predict;
```
### Output
The output of the prediction is an array. Each array element position represents a food class and the value represents a confident rate of prediction. The predicted class is an element with the highest confidence rate.  
``` [[0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]] ```
