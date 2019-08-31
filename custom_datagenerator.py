import os 
import numpy as np
import random

def data_gen(img_folder, mask_folder, batch_size):
    c = 0
    n = os.listdir(img_folder) #List of training images
    random.shuffle(n)
    while (True):
        #img = np.zeros((batch_size, 320, 320, 1)).astype('float')
        #mask = np.zeros((batch_size, 320, 320, 1)).astype('float')
        img = []
        mask = []
        
        for i in range(c, c+batch_size): #initially from 0 to 16, c = 0. 
            #print(i)
            
            # Load X-----------------------
            #train_img = cv2.imread(img_folder+'/'+n[i])/255.
            #train_img =  cv2.resize(train_img, (512, 512))
            
            # load data
            train_img = np.load("{}/{}".format(img_folder, n[i]))
            #print("{}/{}".format(img_folder, n[i]))
            # reshape
            train_img = train_img.reshape(320, 320, 1)
            #img[i-c] = train_img  #add to array - img[0], img[1], and so on.
            img.append(train_img)
            
            # Load Y-----------------------
            #train_mask = cv2.imread(mask_folder+'/'+n[i], cv2.IMREAD_GRAYSCALE)/255.
            #train_mask = cv2.resize(train_mask, (512, 512))
            #train_mask = train_mask.reshape(512, 512, 1)
        
            train_mask = np.load("{}/{}".format(mask_folder, n[i]))
            #print("{}/{}".format(mask_folder,n[i]))
            train_mask = train_mask.reshape(320, 320, 1)
            #mask[i-c] = train_mask
            mask.append(train_mask)
            
        
        img = np.array(img)
        mask = np.array(mask)
        
        #if batch_size >= c+batch_size:
            #break
        print(img.shape, "-----", mask.shape)

        c+=batch_size
        if(c+batch_size>=len(os.listdir(img_folder))):
            c=0
            random.shuffle(n)
            print("Shuffling again")
    
    yield img, mask

# Set dataset directories
train_frame_path = 'dataset/high'
train_mask_path = 'dataset/low'

#x, y = data_gen(train_frame_path, train_mask_path, batch_size = 4)
#x.shape, y.shape
#x[0].shape
#import matplotlib.pyplot as plt
#plt.imshow(x[0].reshape(320, 320))


# Train the model using custom datagen
train_gen = data_gen(train_frame_path, train_mask_path, batch_size = 4)
train_gen


#x, y = iter(train_gen)
#m.fit_generator(train_gen, epochs=NO_OF_EPOCHS, 
#                          steps_per_epoch = (NO_OF_TRAINING_IMAGES//BATCH_SIZE),
#                          validation_data=val_gen, 
#                          validation_steps=(NO_OF_VAL_IMAGES//BATCH_SIZE), 
#                          callbacks=callbacks_list)


# Data generators: #https://towardsdatascience.com/a-keras-pipeline-for-image-segmentation-part-1-6515a421157d
# More about yield in python: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do