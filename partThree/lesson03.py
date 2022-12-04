#coding:utf-8

# 函数式编程
# - 在python中函数是一等对象
# - 一等对象有如下特点
#   - 对象是在运行时创建的
#   - 能赋值给变量或作为数据结构中的元素
#   - 能作为参数传递
#   - 能作为返回值返回
# 高阶函数
# - 高阶函数要符合以下条件中的一个
#   - 接收一个或多个函数作为参数
#   - 将函数作为返回值返回

l = [1,2,3,4,5,6,7,8,9,10]

def fn2(i:int)->bool:
    if i % 2 == 0 :
        return True
    return False

def fn3(i:int)->bool:
    if i > 5 :
        return True
    return False

def fn(func,lst:list)->list:
    '''
        fn(lst:list)->list 可以将列表中的偶数提取并返回
    '''
    new_list = []

    for n in lst :
        if func(n) :
            new_list.append(n)
    
    return new_list

print(fn(fn2,l))
print(fn(fn3,l))


# 匿名函数  lambda 表达式
#   语法： lambda 参数列表 :  返回值
#   可以将匿名函数赋值给变量

print(fn(lambda i : i%2==0 , l))
print(fn(lambda i : i>5 , l))


# 闭包
# 函数嵌套
# 将内部函数作为返回值返回

def fnc() :
    # 定义一个内部函数
    def inner() :
        print("inner")
    return inner
print(fnc())