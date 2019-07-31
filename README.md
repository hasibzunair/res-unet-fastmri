The project is structured as follows.

### Codebase structure
```
dataset # training data provided by competition
fastMRI # fastMRI github repository for helpers and utils


# notebooks and python scripts
*.ipynb 
*.py

```
#### Dataset directory strucuture:

```
dataset/
	singlecoil_train/
			# *.h5 files of MRI data
            
    singlecoil_test_v2/
            # *h5 raw test samples
            
    singlecoil_train_3D_images_48x/
                            low/
                                # undersampled 3D image volumes
                            high/
                                # ground truth 3D  image volumes
                            
```

More details coming sooooon!
