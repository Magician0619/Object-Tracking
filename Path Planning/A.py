#coding=utf-8
import math
import cv2
import numpy as np

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
  file = open(filename,'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    # s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
    s = s +  '\n'
    file.write(s)
  file.close()
  print("保存文件成功") 

def pic2list(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    a = binary
    img_list = a.tolist()#将图片转换成数组列表格式
    text_save("Path Planning/maze3.txt",img_list)
    return img_list

# 启发距离, 当前点和目标点的启发距离; -- 就是简单的曼哈顿距离
def heuristic_distace(Neighbour_node,target_node):
    H = abs(Neighbour_node[0] - target_node[0]) + abs(Neighbour_node[1] - target_node[1])
    return H

def go_around(direction):
    box_length = 1
    diagonal_line = box_length * 1
    if (direction==0 or direction==2 or direction==6 or direction==8):
        return diagonal_line
    elif (direction==1 or direction==3 or direction==4 or direction==5 or direction==7):
        return diagonal_line

def find_coordinate(map,symble):
    #store coordinate
    result=[]
    for index1,value1 in enumerate(map):
        if symble in value1:
            row = index1
            for index2, value2 in enumerate(map[index1]):
                if symble==value2:
                   column = index2
                   result.append([row, column])
    return result

def show_map(map):
    for idx in map:
        print (idx)

# map =[[".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
#       [".", ".", "#", ".", ".", "#", ".", "#", ".", "#"],
#       ["s", ".", "#", ".", "#", ".", "#", ".", ".", "."],
#       [".", "#", "#", ".", ".", ".", ".", ".", "#", "."],
#       [".", ".", ".", ".", "#", "#", ".", ".", "#", "."],
#       [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
#       [".", "#", ".", ".", ".", "#", "#", ".", "#", "."],
#       [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
#       [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
#       [".", ".", ".", "#", "#", "#", ".", ".", "#", "f"],
#       ["#", "#", ".", ".", "#", "#", "#", ".", "#", "."],
#       [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
#       [".", ".", ".", ".", "#", "#", ".", ".", "#", "."]]

img = cv2.imread("hsv_img/46.jpg")
img_final = img 
map = pic2list(img)
img_final_list = map 

#these datas are store in the form of list in a singal list
# 记录所有的障碍物点 坐标
# obstacle = find_coordinate(map,"#")
# start_node = find_coordinate(map,"s")[0]
# target_node = find_coordinate(map,"f")[0]
# current_node = start_node
obstacle = find_coordinate(map,"255")
# start_node = [240,160]
# target_node = [0,160]
start_node = [237,176]
target_node = [2,74]
current_node = start_node

# 设置路径起点为当前节点
path_vertices = [start_node]

#visited_vertices should be stored in the form of a singal list
Neighbour_vertices = []


# 进入查找
while current_node != target_node:

    x_coordinate = current_node[0]
    y_coordinate = current_node[1]
    F = []  # 节点权值 F = g + h
    Neighbour_vertices =   [[x_coordinate - 1, y_coordinate - 1],
                            [x_coordinate - 1, y_coordinate    ],
                            [x_coordinate - 1, y_coordinate + 1],
                            [x_coordinate,     y_coordinate - 1],
                            [x_coordinate    , y_coordinate    ],
                            [x_coordinate,     y_coordinate + 1],
                            [x_coordinate + 1, y_coordinate - 1],
                            [x_coordinate + 1, y_coordinate    ],
                            [x_coordinate + 1, y_coordinate + 1]]
    # 遍历相邻坐标
    for index, value in enumerate(Neighbour_vertices):
        if value[0] in range(len(map)):
            if value[1] in range(len(map)):
               if value not in obstacle+path_vertices:
                    # 如果满足节点 1, 在地图边界内 2, 不在障碍物点和已经经过的点, 计算权重
                    F.append(heuristic_distace(value, target_node) + go_around(index))
                    map[value[0]][value[1]] = str(F[-1])
               else:
                    F.append(10000)
            else:
                    F.append(10000)
        else:
                    F.append(10000)
               #a very large number

    # print(F) # 打印出遍历的 节点的权重
    #将当前点设置为 权重最小的点
    current_node=Neighbour_vertices[F.index(min(total_distance for total_distance in F))]
    map[current_node[0]][current_node[1]] = str(min(F))
    img_show = cv2.circle(img,(current_node[1],current_node[0]), 2, (0, 0, 255))
    # show_map(map)
    print(len(path_vertices))
    path_vertices.append(current_node)
      # if current_node not in visited_vertices:
      #     visited_vertices.append(current_node)
      # else:
      #     print("there is no route between")
      #     break

print(path_vertices)

cv2.imshow("DEBUG",img_show)
cv2.waitKey(0)

