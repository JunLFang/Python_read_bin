import matplotlib.pyplot as plt
import numpy as np

def read_bin(bin_file, width, height, dtype):
    with open(bin_file, 'rb') as fin:
        img = np.fromfile(fin, dtype=dtype)
        img = img.reshape((int(height), int(width),3))
        return img

# path = "path to img RGB stream,but it is one line data , need to reshape, each piexl of img is uint8/int16..."
path ="xxxxxxxx.bin"
height=1080
width=1920
img_c = read_bin(path,width,height,np.uint8)
plt.imshow(img_c)
plt.show()