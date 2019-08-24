''' fastMRI helper script'''
import os 
import matplotlib.pyplot as plt

def create_directory(directory):
    '''
    Creates a new folder in the specified directory if the folder doesn't exist.
    INPUT
        directory: Folder to be created, called as "folder/".
    OUTPUT
        New folder in the current directory.
    '''
    if not os.path.exists(directory):
        os.makedirs(directory)
        
        
def get_number(filename):
    return int(filename[:filename.find('.')])

def sort_paths(paths):
    paths.sort(key = get_number)
    return paths


def normalize(image):
    flat = image.flatten()
    MIN_BOUND = min(flat)
    MAX_BOUND = max(flat)
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image>1] = 1.
    image[image<0] = 0.
    return image

def plot_hist(img):
    img_flat = img.flatten()
    print(min(img_flat), max(img_flat))
    plt.hist(img_flat, bins=20, color='c')
    plt.title("Original input data distribution")
    plt.xlabel("Raw")
    plt.grid(True)
    plt.ylabel("Frequency")
    plt.show()