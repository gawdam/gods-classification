# Gods Classification

This project is an attempt at developing a repository for mythical figures. 
The classification is done by a 3-layer CNN model, which takes an RGB image as an input. 



## Data Collection

~500 images per class was collected from google images by searching for <class_name>+"idol". 
Chrome extension used to batch download: 'Download all images'

Following are the classes:
- Brahma
- Hanuman
- Ganesha
- Shiva
- Vishnu


## Model training

Please refer to "Final Model" section if you want to see the final parameters chosen.

In this secion, all the tuning parameters are listed. A multitude of experiments were conducted on the following parameters. 


- Image-Channels : RGB | Greyscale
- Image-resolution : 200x200 | 400x400
- Image-cropping (to square) : Stretch | Add black pixels
- Image-augmentation : x,y translation | Zoom | Rotation
- Model-architecture : 3 layer
- Model-convolution : 3x3 Same padding with ReLu | 3x3 No padding with ReLu
- Model-activation : Softmax
- Training-callback : Checkpoint | LR Decay | Weighted loss | Regularization | AUC logging
- Training-optimizer : Adam | SGD
- Training-loss : CategoricalCrossEntropy
- Training-dataset : Abalation
- Evaluation-metric : Accuracy | Precision(with declassification threshold) |Avg ROC-AUC

Visit [training logs spreadsheet](https://docs.google.com/spreadsheets/d/14M4bjHU0hTsIOE5Kg2HED66Pj8S2rfyHNIVaIluxvsc/edit?usp=sharing) to learn more.


## Final Model

- Image: RGB - 400x400 - black pixel cropping
- Model: 3 layer 3x3 No padding with softmax activation
- Training: SGD Optimizer with CategoricalCrossEntropy loss
- Evaluation: Evaluated on precision with declassification threshold of 0.6


## App in GCP

[identify-the-god.appspot.com](http://identify-the-god.appspot.com)

