
# coding: utf-8

# # Evaluador
# ***

# In[3]:

#get_ipython().magic('matplotlib inline')


# In[4]:

from darkflow.net.build import TFNet
import cv2


# In[ ]:

#import matplotlib.pyplot as plt
#from skimage import io
import numpy as np


# ## Cargamos YOLO

# In[ ]:

options = {"model": "cfg/yolo.cfg", "load": "weights/yolo.weights", "threshold": 0.4}

tfnet = TFNet(options)


# ## Cargamos algunas imágenes

# In[ ]:

results = []
images = []
images_path = ["./test/000001.jpg",
               "./test/varios.jpg",
               "./test/dog.jpg",
               "./test/dogs.jpg", 
               "./test/selfie2.jpg",
               "./test/niebla.jpg",
               "./test/birds.jpg",
               "./test/cars.jpg",
               "./test/cebras.jpg",
               "./test/indoor.jpg"]

for image_path in images_path:
    images.append(io.imread(image_path))
    results.append(tfnet.return_predict(images[len(images)-1]))


# ## Las mostramos

# In[ ]:

# Mostramos las imagenes resultantes
#fig, axes = plt.subplots(nrows=len(images_path), figsize=(32, 32))

for result, ax, img in zip(results, axes, images):    
    ax.imshow(img)
    ax.axis('off')
    for label in result:
        topleft = label['topleft']
        bottomright = label['bottomright']

        height = bottomright['y'] - topleft['y']
        width = bottomright['x'] - topleft['x']

        coord = [topleft['x'], topleft['y'], width, height]

        #ax.add_patch(plt.Rectangle((topleft['x'], topleft['y']), width, height, edgecolor='red',
                                   #alpha=0.3, lw=2, facecolor='none'))
        ax.annotate(label['label'].capitalize(), xy=(topleft['x'], topleft['y']), xytext=(topleft['x'], topleft['y']))


# ## Ejemplo del resultado de una predicción

# In[ ]:

print(results[0])


# In[ ]:




# In[ ]:



