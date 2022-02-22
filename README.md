# Gods Classification

This project is an attempt at developing a repository for mythical figures. 
The classification is done by a 3-layer CNN model, which takes an RGB image as an input. 



## Data Collection

~500 images per class was collected from google images by searching for <class_name>+"idol". 
Chrome extension used to batch download: 'Download all images'

Following are the classes:
- Brahma

![1-500x500](https://user-images.githubusercontent.com/19368262/155070249-dd50ec71-d8ec-4643-8d38-eb5015869c4f.jpg)

- Hanuman

![1](https://user-images.githubusercontent.com/19368262/155070310-6760f4bf-2090-4f3a-9309-5a6f8428a182.jpg)

- Ganesha

![3d094debf7eddcc011a71b892188dc59](https://user-images.githubusercontent.com/19368262/155070290-ad2debaa-197a-444f-973a-5ec2cf54725f.jpg)

- Shiva

![1-Seated-Shiva-With-Trident-Statue](https://user-images.githubusercontent.com/19368262/155070333-5a880e53-abf4-485d-849c-dcd8de7a9485.jpg)

- Vishnu

![1-Brass-Vishnu-Carving-With-Garuda](https://user-images.githubusercontent.com/19368262/155070355-497ffc64-06bf-4d0d-bbe5-5c65e25b5b98.jpg)

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
- Evaluation-metric : Accuracy | Precision(with declassification threshold) | Avg ROC-AUC

Visit [training logs spreadsheet](https://docs.google.com/spreadsheets/d/14M4bjHU0hTsIOE5Kg2HED66Pj8S2rfyHNIVaIluxvsc/edit?usp=sharing) to learn more.


## Final Model

Train-validation-test split : 72%-18%-10%

![image](https://user-images.githubusercontent.com/19368262/155069292-95a9e859-a4b5-42e3-a051-bc2c203c63b9.png)

- Image: RGB - 400x400 - black pixel cropping
- Model: 3 layer 3x3 No padding with softmax activation
- Training: SGD Optimizer with CategoricalCrossEntropy loss
- Evaluation: Evaluated on precision with declassification threshold of 0.6

## Model Evaluation

- Confusion Matrix

![image](https://user-images.githubusercontent.com/19368262/155069393-2b90a27c-4f90-4460-bccf-43ff5a18ad40.png)

- ROC curve

![image](https://user-images.githubusercontent.com/19368262/155069512-bd2081c7-bbf6-4ed4-aff9-c17a7ab87dd7.png)

- Classification confidence histogram

![image](https://user-images.githubusercontent.com/19368262/155069617-1400eecf-7519-41a3-9432-a44047021848.png)


## App in GCP

[identify-the-god.appspot.com](http://identify-the-god.appspot.com)

