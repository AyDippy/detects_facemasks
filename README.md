# Face Mask Detection Project

This project is focused on detecting whether people in images are wearing face masks, and if so, whether they are wearing them correctly or incorrectly.

## Dataset

The dataset used for this project was obtained from Kaggle and consists of two main folders:

- **Images Folder**: Contains the images of people with and without face masks.
- **Annotation Folder**: Contains XML files with annotations corresponding to each image.

You can access the dataset on Kaggle [here](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection).

## Data Preparation

In the `data_preparation` folder of this repository, you can find the Python code used to process and split the dataset into three categories:

- "No Mask": Images of people without masks.
- "Face Mask On": Images of people correctly wearing face masks.
- "Face Mask Worn Wrongly": Images of people with improperly worn face masks.

Additionally, the dataset was further divided into a training set (70%) and a validation set (30%) for model training. You can access these sets on Google Drive:

- [Training Set](https://drive.google.com/drive/folders/1A0PqTUBISlz6fLdSDcBR9iIiyzvslpBk?usp=sharing)
- [Validation Set](https://drive.google.com/drive/folders/1OJpH6mZxB7YxK3hNnqHLhAjrT05efX-U?usp=sharing)

## Model Architecture

The model architecture for this project is based on the VGG16 model. After importing the pre-trained VGG16 model, additional layers were added to classify the features extracted by VGG16. The model was then trained using the training set.

## Training

The model was trained for 30 epochs, and it achieved an accuracy of approximately 80%. Keep in mind that the dataset size may have influenced the final accuracy due to its limited size.

## Contact

If you have any questions or would like to get in touch, feel free to contact me:

- Email: [ayomidedipeolu@gmail.com](mailto:ayomidedipeolu@gmail.com)
- GitHub: https://github.com/AyDippy)https://github.com/AyDippy
