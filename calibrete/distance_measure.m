u=input('请输入图像中目标点的横坐标（注意像素范围）:');
v=input('请输入图像中目标点的纵坐标（注意像素范围）:');
cameraParams = calibrationSession.CameraParameters;
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