# Person detection from aerial drone

This project is a part of my Bachelor thesis at [CS department](https://cs.hse.ru/en/) of the Higher school of Ecominics.


### Project description

Every year in Russia alone more than 10 000 people get lost, and around 10% of them are found dead because the search lasted too long. The main goal of this project is to develop an algorithm which automates person detection on aerial images taken by drone over the lost person search area. My baseline algorithm is Mask R-CNN, state-of-the-art model in object detection. In my work I use the implementation of this network from [matterport repository](https://github.com/matterport/Mask_RCNN).

As it often appears in practice, I was not able to find datasets which are suitable for the evaluation of model performance. The area of lost person search is typically located somewhere in forests or fields, while most datasets of aerial images contain images of urban landscapes. Therefore, a part of my work is devoted to the generation of synthetic datasets, similar to aerial images, which are typically taken during lost person search. In [synthetic_dataset.ipynb notebook](https://github.com/katyamineeva/person-detection-from-aerial-drone/blob/master/synthetic_dataset.ipynb) you can find the details of the algorithm for synthetic data generation.

In further experiments, I evaluate the performance of the Mask R-CNN on created synthetic datasets and also compare it with RetinaNet —  the implementation is taken from [fizyr repository](https://github.com/fizyr/keras-retinanet). For evaluation I use metrics tools provided in [rafaelpadilla repository](https://github.com/rafaelpadilla/Object-Detection-Metrics). The results obtained are show in [models_testing.ipynb notebook](https://github.com/katyamineeva/person-detection-from-aerial-drone/blob/master/models_testing.ipynb).
