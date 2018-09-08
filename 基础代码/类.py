# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def getname(self):
#         return self.name
# stu = Student('john',23)
# print(stu.getname())


# 封装好变量只能在类的内部修改
# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     # 获取姓名
#     def getname(self):
#         return self.__name
#     def updatename(self,name):
#         self.__name = name
# stu = Student('john', 23)
# print("修改之前\n"+stu.getname())
# stu.updatename('bohongtao')
# print("修改之后\n"+stu.getname())

# 继承与重写
class Animal(object):
    def run(self):
        print('这是父类的方法')
class Dog(Animal):
    def run(self):
        print('这是重写的子类的方法')

dog = Dog()
dog.run()