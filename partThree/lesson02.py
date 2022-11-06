#coding:utf-8
# 作用域（scope）
# 变量生效的区域

def fn():
    a = 10 # 函数内变量，函数外无法使用
    print(a)
fn()
# print(a)

# 在python 有两种作用域：全局作用域，函数作用域
# 全局作用域在程序执行时创建，在程序结束时销毁（所有函数以外的区域）
# 函数作用域在函数调用时创建，调用完销毁

b = 10

def fn1():
    # 如果在函数中希望改变全局变量，需要使用global来声明
    global b
    b = 20
    print(b)
fn1()
print(b)