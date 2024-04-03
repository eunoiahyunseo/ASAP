import numpy as np
from PIL import Image
import os


path_dir = 'Shooting7/'# '' 안에 파일을 묶고 있는 "폴더 경로"를 쓰세요
file_list = os.listdir(path_dir)
i='a'
cnt=0
for png in file_list:
    image = Image.open(path_dir + png)
    pixel = np.array(image)
    png = png.split('.')[0]
    cnt+=1
    if cnt%100 == 0:
        i = chr(ord(i)+1)
    np.save("numpy/"+str(i)+"/"+png, pixel) #저장할 '폴더 경로'를 쓰세요
