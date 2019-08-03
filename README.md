## fastMRI Image Reconstruction Challenge 2019.

The project is structured as follows.

## Challenge description

## Dependencies
This work is implemented in Python 3.6 and Keras using Tensorflow as backend.

*    Ubuntu 14.04
*    Python 3.6

## Directory strucuture and usage
* `media` : Contains supporting material for README.md
* `dataset` : training data provided by competition
* `fastMRI` : fastMRI github repository for helpers and utils
* *.ipynb # notebooks and python scripts
* *.py

## Dataset directory strucuture:

```
dataset/
    singlecoil_train/
                # *.h5 files of MRI data
    singlecoil_test_v2/
                # *h5 raw test samples
    # preprocessed
    singlecoil_train_3D_images_48x/
                                low/
                                    # undersampled 3D image volumes
                                high/
                                    # ground truth 3D  image volumes
                           
```

## Data

Here is a single MRI scan showing both undersampled and ground truth.

![](media/mri_high.gif) | ![](media/mri_low.gif)

More details coming sooooon!
