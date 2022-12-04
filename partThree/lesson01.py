#coding:utf-8
# 函数

# 定义一个函数
def fn() :
    print("这是第一个函数！")
    print("hello")

fn()

# 求阶乘
def fn2(n)->int:
    if n==1 :
        return 1
    else :
        return n * fn2(n-1)

a = fn2(5)
print(a)

# 实参的传递方式
# 位置参数，按位置来传递
# 关键字参数，可以不按顺序来传递
# 关键字参数可以和位置参数混合使用，位置参数必须位于关键字参数之前
def fn3(a,b,c = 20) :
    print(a,' ',b,' ',c)

fn3(1,2)
fn3(a=3,c=1,b=0)

# 实参类型
# 函数调用时，解释器不会检查实参类型
def fn4(a) :
    # 函数中赋值，不影响其他变量
    a = 20
    print(a)

c=10
fn4(c)
print(c)

# 不定长参数
# 不定长参数只能有一个
# 求任意个数的和
def fn5(*a)->int:
    ans = 0
    for i in a:
        ans = ans + i
    return ans
a = fn5(1,2,3,4,5,6,7,8,9,10)
print(a)

# *的参数之后的参数必须以关键字形式传递
def fn6(a,*b,c):
    print (a,' ',b,' ',c)
fn6(1,2,3,4,c=5)

# **形参可以接收其他的关键字参数，保存到字典中，键是参数名，值是参数值
# 只能有一个，必须写在所有参数的最后
def fn7(**a) :
    print(a)

fn7(a = 12,b = 23,c = 34)


# 参数解包
def fn8(a,b,c):
    print(a)
    print(b)
    print(c)
fn8(1,2,3)
t = (10,20,30)
# 添加*解包，要求参数个数与形参个数一致
fn8(*t)

d = {'a':20,'b':30,'c':50}
fn8(**d)

# 返回值可以是一个函数
def fn9():
    def fn():
        print("hello")
    return fn
r = fn9()
print(r,' ',type(r))

# 文档字符串，是对函数的说明
# 在函数第一行写一个字符串即可
# 定义时可以加上类型说明，不是强制指定类型
def fn10(a:int,b:int)->int:
    '''
    用来求两数之和
    需要传入两个数字
    '''
    return a+b
help(fn10)