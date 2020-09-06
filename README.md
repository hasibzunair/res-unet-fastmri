# fastMRI Image Reconstruction Challenge 2019 (4x single-coil track)

![](media/mri_low.gif) | ![](media/mri_high.gif)

The project is structured as follows.

### Challenge description

Given an undersampled MRI scan, the goal is to reconstruct a high resolution MRI scan. 

### Dependencies
This work is implemented in Python 3.6 and Keras using Tensorflow as backend.

*    Ubuntu 14.04
*    Python 3.6

### Directory strucuture and usage
* `media` : Contains supporting material for README.md
* `dataset` : training data provided by competition
* `fastMRI` : fastMRI github repository for helpers and utils
* *.ipynb # notebooks and python scripts
* *.py

### Dataset directory strucuture:

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

### Results

Our final submission logs are shown below. Among the other participants which came through to the final leaderboard, we were last!

![](media/final_result.png)




