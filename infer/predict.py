# -*- coding: utf-8 -*-

import numpy as np
import paddle
from PIL import Image
import cv2

import numpy as np;
import os

import paddle
import paddle.fluid as fluid

crop_size = 128
resize_size = 128


# image_dir = "/Volumes/External/EB/EB_result/result_camera_4";
# image_dir = "/Volumes/External/EB/camera_1";
image_dir = "predict/img"


model_dir = "0818_overtake_test/model_infer"
place = fluid.CPUPlace()
exe = fluid.Executor(place)
[program, feed, fetch] = fluid.io.load_inference_model(model_dir, exe, model_filename='model', params_filename="params")


def save_float(path, array):
    f = open(path, 'w+')
    for i in range(0, len(array)):
        # print(array[i])
        # a = struct.pack('f',array[i]);
        f.write(str(array[i]))
        f.write("\n")
    f.close();
    print("done")

def preprocess(img):
    # img = Image.open(path)
    # 统一图像大小
    img = img.resize((resize_size, resize_size), Image.ANTIALIAS)
    # img = img.resize((crop_size, crop_size), Image.ANTIALIAS)
    img = np.array(img).astype(np.float32)
    #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # 转换成CHW
    transed = img.transpose((2, 0, 1))
    # 转换成BGR
    transed = transed[(2, 1, 0), :, :] / 255.0
    return transed, img


def infer(name):
    image_path = image_dir + "/" + name;
    # image_path = "/home/aistudio/524.jpg";
    print(image_path)
    src = Image.open(image_path)

    img, origin = preprocess(src)
    input_data = img[np.newaxis, :]
    
    # print(img)

	
#     input_data = np.zeros((1, 3, crop_size, crop_size), dtype=np.float32)
# 	# input_data[0, 0:img.shape[0], offset:img.shape[1] + offset, 0:img.shape[2]] = img
#     input_data[0, 0:img.shape[0], 0:img.shape[1] + 0, 0:img.shape[2]] = img

#     with open('ss.txt', 'w+') as the_input_file:
#         for x in np.nditer(input_data):
#             the_input_file.write('%f\r\n' % x)

    cv2.imwrite("ss.jpg", origin);
    # input_data = np.zeros((1, 3, crop_size, crop_size), dtype=np.float32)
    results = exe.run(program=program,
                          feed={feed[0]:input_data},
                          fetch_list=fetch,return_numpy=False)

    for i in range(0,len(fetch)):
        print (fetch[i].name);
        m = 0;
        # with open(str(i) + "/" + name + '.txt', 'w+') as the_input_file:
        #     for x in np.nditer(results[i]):
        #         pass
        #         # the_input_file.write('{}\n'.format(x))
        print ("max:{}".format(m))
    print(len(results))
    results = np.array(results[0])
    # print(results * 300 + 1500)
    print(results*600 + 1200)
for i in range(2000):
    infer(str(i)+".jpg");