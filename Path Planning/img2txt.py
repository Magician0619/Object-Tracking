import cv2

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
  file = open(filename,'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    # s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
    s = s +  '\n'
    file.write(s)
  file.close()
  print("保存文件成功") 


img = cv2.imread("Path Planning/0.jpg")

cv2.imread()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

a = binary
print("check img shape",a.shape)
cv2.imshow("djfks",a)
img_list = a.tolist()#将图片转换成数组列表格式
text_save("Path Planning/maze2.txt",img_list)
print(img_list)
cv2.waitKey(0)