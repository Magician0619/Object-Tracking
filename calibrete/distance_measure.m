u=input('������ͼ����Ŀ���ĺ����꣨ע�����ط�Χ��:');
v=input('������ͼ����Ŀ���������꣨ע�����ط�Χ��:');
cameraParams = calibrationSession.CameraParameters;
%% ��ȡmatlab����궨�����������������ÿ��ͼƬ��Ӧ��һ���������ѡ����ʵ���������ϵ������Чʵ�ֲ��
in = cameraParams.IntrinsicMatrix'; 
R = cameraParams.RotationMatrices(:,:,3);
t = cameraParams.TranslationVectors(3,:)';
u0 = in(1,3);
v0 = in(2,3);
f_dx = in(1,1);
f_dy = in(2,2);
R1=R(1,1);R2=R(1,2);R4=R(2,1);R5=R(2,2);R7=R(3,1);R8=R(3,2);
t1=t(1);t2=t(2);t3=t(3);

%%�������ص㣨u,v����Ӧ����������ϵ���룬ͨ�����ʵİڷ�Ҳ���������������ĺ��������
A=(u-u0)*R7-f_dx*R1;  B=(u-u0)*R8-f_dx*R2;  C=(u-u0)*t3-f_dx*t1;
D=(v-v0)*R7-f_dy*R4;  E=(v-v0)*R8-f_dy*R5;  F=(v-v0)*t3-f_dy*t2; 

X=(C*E-B*F)/(B*D-A*E);
Y=(A*F-C*D)/(B*D-A*E);
disp(['�������Ϊ',num2str(X/10),'cm']);
disp(['�������Ϊ',num2str(Y/10),'cm']);