# L = [];
# for x in range(1,11):
# 	L.append(x*x);
# print(L);
# print([x * x for x in range(1,11)]);
# 
# 打印出当前目录文件
import os;
print([d for d in os.listdir('.')]);
