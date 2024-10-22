import numpy as np
import os, re
import numpy as np
import cv2 as cv
from sys import argv
import getopt

path = os.path.split(os.path.realpath(__file__))[0]+"/.."
#script, vels = argv
opts,args = getopt.getopt(argv[1:],'-hH',['img_path=','save_path='])
#print(opts)

img_path = "img"
save_path = "hsv_img"


#camera = "/dev/video0"

for opt_name,opt_value in opts:
    if opt_name in ('-h','-H'):
        print("python3 Img_Handle.py  --img_path=img   --save_path=hsv_img")
        exit()

    if opt_name in ('--img_path'):
        img_path  = opt_value

    if opt_name in ('--save_path'):
        save_path = opt_value

    
        #print("camera.value=",camera.value)


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("----- new folder -----")
    else:
        print('----- there is this folder -----')

def img_extract(img_path, save_path):
    img_name = os.listdir(img_path)

    # Threshold of yellow lane
    lower_race = np.array([25, 75, 165])
    upper_race = np.array([40, 255, 255])
    # Threshold of red cone
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([20, 255, 255])


    for img in img_name:
        print(img)
        image = os.path.join(img_path, img)
        src = cv.imread(image)
        hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

        race_mask = cv2.inRange(hsv, lower_race, upper_race)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)

        race_res = cv2.bitwise_and(frame, frame, mask = race_mask)
        red_res = cv2.bitwise_and(frame, frame, mask = red_mask)
        res = race_res + red_res
        
        ind = int(re.findall('.+(?=.jpg)', img)[0])
        new_name = str(ind) + '.jpg'
        cv.imwrite(os.path.join(save_path, new_name), mask)


if __name__ == "__main__":
    
    img_path = path + "/data/"+ img_path
    save_path = path + "/data/"+ save_path
  
    mkdir(save_path)
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    img_extract(img_path, save_path)

