#coding:utf-8

# 继承
class Animal:
    def __init__(self,name) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self,name:str) -> None:
        self._name = name

    def run(self) ->None:
        print("跑。。。。")

    def sleep(self) -> None:
        print("睡觉zzz")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def bark(self) -> None:
        print("汪。。。")

    # 重写父类方法
    def sleep(self) -> None:
        print("在狗窝里睡zzzz")

dog = Dog("旺财")
dog.run()
dog.sleep()
dog.bark()

print(issubclass(Dog,Animal))
print(issubclass(Animal,Animal))