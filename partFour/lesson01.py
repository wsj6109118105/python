#coding:utf-8

# 类
#   - 语法：class 类名([父类]) :
#           代码块

class MyClass():
    pass

mc = MyClass()
# print(mc)

# isinstance()用来检查一个对象是否是一个类的实例

# result = isinstance(mc,MyClass)
# print(result)
# mc.name = '龙城飞将'
# print(mc.name)


# 人类
class Person():
    # 在类中可以定义变量和函数，在类中定义的变量，会成为所有实例的公共属性，所有实例都可以访问这些变量
    name = '龙城飞将'
    # 定义方法，方法在调用时默认解析器会传第一个参数
    def say_hello(self) :
        print('你好,%s'%self.name)

p1 = Person()
p1.name = "哈哈哈"
p2 = Person()
p2.name = '呵呵呵'
print(p1.name)
print(p2.name)

del p2.name  # 删除p2的name属性
print(p2.name)
