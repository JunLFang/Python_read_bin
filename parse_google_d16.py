import matplotlib.pyplot as plt
import numpy as np


### 如何read google 定义的d16的数据
def read_bin(bin_file, width, height, dtype):
    with open(bin_file, 'rb') as fin:
        img = np.fromfile(fin, dtype=dtype)
        print(img[0:8])   ###前8字节是embedded的data
        img = img[8:]
        img = img.reshape((int(height), int(width)))
        return img


path_d = "xxxxx"

img = read_bin(path_d,240,180,np.int16)

img_conf = img&0xE000>>13
img_depth = img & 0x1FFF

fig, axs = plt.subplots(1, 2)
axs[0].imshow(img_depth)
axs[0].set_xlabel('depth')

axs[1].imshow(img_conf)
axs[1].set_xlabel('conf')
plt.show()