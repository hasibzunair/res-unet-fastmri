import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import pylab
import cv2
from fastMRI.data import transforms as T

'''
Fancy program which shows the MRI scan slice by slice
'''

# the MRI scan from the folder
image_number = "1"


img_3d = np.load("/home/hasib/MRI-reconstruction/dataset/singlecoil_train_3D_images_48x/high/{}.npy".format(image_number))
img_3d = T.to_tensor(img_3d)
img_3d, _, _ = T.normalize_instance(img_3d)
img_3d = np.abs(img_3d.numpy())

print(img_3d.shape)
print("p(UP) and l(DOWN) to control slices")

counter = 0
window = np.array((1,2))

# p and l to control slices
while True:
    if counter > 30:
        break
        
    if counter >= img_3d.shape[-1]:
        break
    window = img_3d[counter,:,:]
    #print(window.shape)
    
    cv2.imshow("image 3d".format(counter), window)
    
    k = cv2.waitKey(1) & 0xff
    if k != 255: 
        if k == 112:
            print("forward")
            counter+=1
            # save images
            #cv2.imwrite("{}.jpg".format(counter), window)
            print(counter)
            
        if k == 108:
            print("backward")
            counter-=1
            print(counter)

    if k == 27: 
        break

print("All slices shown")
cv2.destroyAllWindows()