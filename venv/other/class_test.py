class User:
    '''
    User类
    '''
    print ('User类')

#item
class Item:
    print('Item')
    itemtype='est'
    itemcolor="weizhi"
print(Item.itemcolor)
print(Item.itemtype)
Item.too='bal'
print(Item.too)


#构造方法_init_
class Person:
    def __init__(self,name='ca',age=9):
        print('构造函数')
        self.name = name
        self.age = age


p = Person()
#访问实例变量，对象.变量
print(p.name,p.age)

P2 = Person('sdfsg')
print(P2.name,P2.age)

P3= Person(age=30)
print(P3.name,P3.age)

p4 = Person('baigujing',45)
print(p4.name,p4.age)

class Teacher:
    #空类
    pass
