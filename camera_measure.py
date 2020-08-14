import cv2
import math
import numpy as np

'''
%% 根据matlab标定工具箱获取相机的内外参数，内参数只有一个对应的矩阵，
%%而外参数（旋转矩阵和位移矩阵）每一张标定板图像都对应有一个矩阵。
%%针对自动驾驶需求，世界坐标系中目标点的Z轴并非重要参考对象，可以不考虑，提前设置Z=0；
%%综上所述，结合各个坐标系转换方程，编写二维图像坐标系点 推导 三维世界坐标系点（只包含纵向、横向距离）程序
%%特别说明，坐标系转换矩阵中最需要注意的点就是  Zc项，该项来自于世界坐标系向相机坐标系转换所产生
%%外参数的标定板应选择合适的位置，推荐将标定板右下角放置于图像底端中间位置处，便于测距计算

%% 内参用字母 in 表示，放置于地面的标定板对应于求取外部参数，旋转矩阵用R表示，平移矩阵用T表示
%%其中求解过程中会涉及到内参数：每一个像素在 X 轴与 Y 轴方向上的物理尺寸为dx、dy，用字母f_dx,f_dy表示
%%涉及到的内参数： 光心横坐标用u0表示，光心纵坐标用v0表示;
%%涉及到的外参数： 旋转矩阵为3*3大小，具体用R1、R2、R3...R9依次表示；
%%涉及到的外参数： 平移矩阵为3*1大小，具体用t1、t2、t3依次表示；

%% 图像坐标系中的点用（u，v）表示，世界坐标系的位置距离用（X，Y）表示，X代表横向距离，Y代表纵向距离
'''
def measure(u,v):
    fx = 305.6261999368051
    cx = 169.9830363751688
    fy = 344.2600716547944
    cy = 73.945565684040190
    k1, k2, p1, p2, k3 = -0.435917245316158, 0.206260536218705, 0.0, 0.0, 0.0
 
    # 相机坐标系到像素坐标系的转换矩阵
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])

    

'''
%% 获取matlab相机标定后的内外参数，外参数每张图片对应有一个外参数，选择合适的世界坐标系可以有效实现测距
in = cameraParams.IntrinsicMatrix'; 
R = cameraParams.RotationMatrices(:,:,3);
t = cameraParams.TranslationVectors(3,:)';
u0 = in(1,3);
v0 = in(2,3);
f_dx = in(1,1);
f_dy = in(2,2);
R1=R(1,1);R2=R(1,2);R4=R(2,1);R5=R(2,2);R7=R(3,1);R8=R(3,2);
t1=t(1);t2=t(2);t3=t(3);

%%计算像素点（u,v）对应的世界坐标系距离，通过合适的摆放也可以算出距离相机的横纵向距离
A=(u-u0)*R7-f_dx*R1;  B=(u-u0)*R8-f_dx*R2;  C=(u-u0)*t3-f_dx*t1;
D=(v-v0)*R7-f_dy*R4;  E=(v-v0)*R8-f_dy*R5;  F=(v-v0)*t3-f_dy*t2; 

X=(C*E-B*F)/(B*D-A*E);
Y=(A*F-C*D)/(B*D-A*E);
disp(['横向距离为',num2str(X/10),'cm']);
disp(['纵向距离为',num2str(Y/10),'cm']);
'''