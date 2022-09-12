#coding:utf-8
# 列表
# 创建列表：通过[]
# my_list = ["wang","lu","fei",22]
# print(my_list,type(my_list))

# 可以通过索引来获取列表中的元素，索引从0开始
# print(my_list[1])

# 获取列表长度，通过len()函数
# print(len(my_list))

# 切片
# 语法：列表[起始位置：结束位置]   左闭右开
# 做切片操作时会返回一个新的列表
# 起始和结束位置索引可以省略，会从开头截取到结束位置，或者起始位置截取到结尾
# stus = ["孙悟空","猪八戒","沙悟净","唐僧","二郎神","太上老君"]
# print(stus[0:2])
# print(stus[2:])
# print(stus[:3])

# 语法：列表[起始：结束：步长]  步长表示每次获取默认值间隔，默认是1
# 步长不能是0，但可以是负数
# print(stus[0:5:2])
# print(stus[0:5:1])
# print(stus[::-1])
# print(stus[5:0:-2])

# 通用操作

# + 和 *
# + 可以将两个列表拼接成一个列表
# * 可以将列表重复指定的次数
# my_list1 = [1,2,3] + [4,5,6]
# my_list1 = [1,2,3] * 2
# print(my_list1)

# in 和 not in
# in 用来检查指定元素是否在列表中，存在返回True，否则返回False
# not in 检查指定元素是否不在列表中，不在返回True，在返回False
# print("孙悟空" in stus)
# print("玉皇大帝"not in stus)

# len()获取列表中元素的个数
# print(len(stus))

# min(),max()
# min()获取列表中的最小值
# max()获取列表中的最大值
# arr = [1,4,9,123,345,2456]
# print(min(arr))
# print(max(arr))

# index():获取指定元素在列表中的位置
# count():统计指定元素的个数
# print(stus.index("沙悟净"))
# print(stus.count("孙悟空"))

# 通过索引修改元素
# stus[0] = "sunwukong"
# print(stus)

# 通过del删除元素
# del stus[2]
# print(stus)

# 通过切片进行修改，在给切片赋值时，必须传递序列
# 当设置了步长时，序列中元素的个数必须和切片的个数一致，对步长位置进行替换
# 通过del删除
# stus[0:2] = ["sunwukong","zhubajie"]
# stus[0:0] = ["牛魔王"]
# stus[::3] = ["牛魔王","孙悟空"]
# del stus[0:2]
# print(stus)

# 修改操作只适用于可变序列

# 列表的方法
# stus = ["孙悟空","猪八戒","沙和尚"]
# print(stus)

# append():添加到列表最后
# stus.append("唐僧")
# print(stus)

# insert():向列表指定位置插入
# stus.insert(1,"牛魔王")
# print(stus)

# extend():使用新的序列扩展当前序列
# stus.extend(["唐僧","牛魔王"])
# print(stus)

# clear():清空序列
# stus.clear()
# print(stus)

# pop():根据索引删除并返回指定元素
# print(stus.pop(1))
# print(stus)

# remove():删除指定值的元素，如果有多个，只会删除第一个
# stus.remove("猪八戒")
# print(stus)

# reverse():反转列表
# stus.reverse()
# print(stus)

# sort():用来对列表进行排序，默认升序排列
# my_list = list("adsfqwefagdsga")
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
