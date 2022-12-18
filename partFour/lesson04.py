#coding:utf-8

# 封装
class Person:
    def __init__(self,name:str) -> None:
        self._name = name

    # 使用property装饰器来生成get 方法，注意方法名和属性名不能相同，否则会递归调用导致栈溢出
    @property
    def name(self) -> str:
        return self._name

    # 属性.setter来生成set方法
    @name.setter
    def name(self,name) -> None:
        self._name = name

p = Person('大将军')
p.name = '龙城飞将'
print(p.name)