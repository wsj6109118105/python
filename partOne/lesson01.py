#coding:utf-8
#类型转换
#四个函数 int() float() str() bool()
a = True
print("a = ",a)
print("a的类型是",type(a))

a = int(a)
print("a = ",a)
print("a的类型转换之后为",type(a))

a = float(a)
print("a = ",a)
print("a的类型转换之后为",type(a))

a = str(a)
print("a = ",a)
print("a的类型转换之后为",type(a))

a = "11.5"
print("a的类型",type(a))
#a = int(a)    #ValueError: invalid literal for int() with base 10: '11.5'

a = 11.5
print("a的类型为",type(a))
a = int(a)
print("a = ",a)
print("a 的类型为",type(a))

a = None
#a = int(a)    #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
print("a = ",a)
print("a 的类型为",type(a))

a = 10
a = bool(a)
print("a = ",a)

a = -10
a = bool(a)
print("a = ",a)

a = 0
a = bool(a)
print("a = ",a)

a = ""
a = bool(a)
print("a = ",a)

a = None
a = bool(a)
print("a = ",a)   #所有对象都可以转换成bool，表示空的会转成False,其他都会转成True