from __future__ import division
import matplotlib.image as imga
import matplotlib.pyplot as plt
import numpy as np
import math
#inter image location
file=imga.imread("ffdfg.JPG")
img=file
file=np.dot(-1,file)
#plotting color displacement in RGB plane
for i in range(file.shape[0]):
	for j in range(file.shape[1]-1):
		img[i][j][0]=math.sqrt((file[i][j+1][0]-file[i][j][0])**2+(file[i][j+1][1]-file[i][j][1])**2+(file[i][j+1][2]-file[i][j][2])**2)
		img[i][j][1]=img[i][j][0]
		img[i][j][2]=img[i][j][0]
for i in range(file.shape[1]):
	for j in range(file.shape[0]-1):
		img[j][i][0]=math.sqrt((file[j+1][i][0]-file[j][i][0])**2+(file[j+1][i][1]-file[j][i][1])**2+(file[j+1][i][2]-file[j][i][2])**2)
		img[j][i][1]=img[j][i][0]
		img[j][i][2]=img[j][i][0]
img=np.dot(-1,img)
plt.imshow(img)
#name of new mofified file
imga.imsave('newl.jpg', img)
plt.show()
