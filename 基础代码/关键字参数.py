# 关键字参数
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('john',23)
person('john',23,city='济南')

othwers = {'sex':'男'}
person('john',23,**othwers)

