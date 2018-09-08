height = int(input('请输入你的身高cm：'));
weight = int(input('请输入你的体重kg:'));
bmi = weight/height**2;
if bmi<18.5:
   print('太轻了');
elif bmi<25:
	print('正常');
elif bmi<28:
	print('过重');
elif bmi<32:
	print('肥胖');
else:
	print('严重肥胖');	