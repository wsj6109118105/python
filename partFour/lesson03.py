#coding:utf-8

# 封装

class Rectangle():
    '''
        矩形类
    '''
    # 使用双下划线修饰属性，从可以达到隐藏的目的
    # 双下划线修饰的属性会被改名为_类名__属性名
    def __init__(self, width:int,length:int) -> None:
        self.__width = width
        self.__length = length
    
    def set_width(self,width:int) -> None:
        self.__width = width
    
    def get_width(self) -> int:
        return self.__width

    def set_length(self,length:int) -> None:
        self.__length = length

    def get_length(self) -> int:
        return self.__length

rec = Rectangle(2,5)
print(rec.get_length())
print(rec.get_width())
print(rec._Rectangle__width)
