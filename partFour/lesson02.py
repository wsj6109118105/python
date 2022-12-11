#coding:utf-8

# 创建对象流程
#   1.创建一个变量
#   2.在内存中新建一个变量
#   3.类代码块执行（类定义时执行一次）
#   4.__init__方法执行
#   5.将对象的id赋值给变量
# init可以在创建的对象中初始化变量
class Person():
    print("代码块执行")
    def __init__(self,name) -> None:
        self.name = name
    def say_hello(self) -> None:
        print("你好！我是%s"%self.name)

p1 = Person("龙城飞将")
p1.say_hello()