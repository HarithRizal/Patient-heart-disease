# Patient-heart-disease

## 1. Summary
The aim of this project is to create a deep learning model to predict heart disease on patient. The model is trained with [Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## 2. IDE and Framework
The project is built with Collaboratory. The main frameworks used in this project are TensorFlow, Numpy, Pandas and Scikit-learn.

## 3. Methodology

### 3.1 Data Pipeline
The data is first loaded and preprocessed, such that unwanted features are removed, and label is encoded in one-hot format. Then the data is split into train-validation-test sets, with a ratio of 70:30.

### 3.2 Model Pipeline
A feedfoward neural network is constructed that is catered for classification problem. The structure of the model is fairly simple. Figure below shows the structure of the model

![model](https://user-images.githubusercontent.com/108482217/176980880-a4ca12f9-a730-44b9-bd53-1c13e718a123.png)

The model is trained with a batch size of 128 and 100 epochs. Early stopping is also applied in the model training. The training stops at epoch 37, with a training accuracy of 100% and validation accuracy of 100%. The two figures below shows the graph of the training process.

![Accuracy](https://user-images.githubusercontent.com/108482217/176980892-d30cc33c-aefb-4ea3-8b30-d73f007e2392.png)

![loss](https://user-images.githubusercontent.com/108482217/176980900-1beb12f1-2e98-464f-ac58-da8d3f465cc2.png)

## 4. Results
Upon evaluating the model with test data, the model obtaing the following test results, as shown in  figure below.

![evaluation result](https://user-images.githubusercontent.com/108482217/176980905-52aaf1f6-499c-4307-9c6c-db24cc95c2d9.png)
