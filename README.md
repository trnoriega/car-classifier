# Experiments for the Development of [CarMatch](www.thomasnoriega.com/carmatch)

This repository contains the experiments I ran to train an Inception_v3 2D convolutional neural network with the Keras framework (and TensorFlow backend) to accurately classify 196 different cars.  

### Making the dataset usable
In the [1_make_dataset_usable](1_make_dataset_usable.ipynb) notebook I make the [cars dataset](http://ai.stanford.edu/~jkrause/cars/car_dataset.html) usable.

The dataset has 16,185 images classified into 196 different classes of car. Classes are defined as unique combinations of manufacturer, model, and year.

### Characterizing the dataset
In the [2_characterize_the_dataset](2_characterize_the_dataset.ipynb) notebook I characterize the [cars dataset](http://ai.stanford.edu/~jkrause/cars/car_dataset.html) to understand what the manufacturer, model, and year distributions are. I also look at the type, quality and shape of the car photos. 

### Split into train, validation, and test sets
In the [3_train_val_test_split](3_train_val_test_split.ipynb) notebook I split the [cars dataset](http://ai.stanford.edu/~jkrause/cars/car_dataset.html) into a 70/15/15 train/validation/test sets to train the classifier. 

The splitting involves splitting all photos into labeled subfolders so that Keras can use those directly for its image generators.

### Understanding Keras image augmentation
In the [4_image_augmentation](4_image_augmentation.ipynb) notebook I visually show what the in-memory image augmentation transformation I will implement in Keras during training will look like.

### Training experiments
The notebooks contained in the  [inception_v3_experiments](inception_v3_experiments) folder, and summarized in the [1_Inceptionv3_summary](inception_v3_experiments/1_Inceptionv3_summary.ipynb) are where the actual experiment notebooks reside. The final model used in the CarMatch product can be found in the [Inceptionv3_21.ipynb](inception_v3_experiments/Inceptionv3_21.ipynb) notebook

### Model Validation
In the [5_model_validation](5_model_validation.ipynb) notebook I show that the final model has a __top-1 accuracy of ~77% and a top-5 accuracy of ~95%__. I also look at f1 and AUROC metrics. 

### Improving the results
In the [6_result_optimization](6_result_optimization.ipynb) notebook I show that by developing an algorithm that considers the most represented body-styles in combination with the highest confidence results I can provide results that are more useful for the CarMatch user.