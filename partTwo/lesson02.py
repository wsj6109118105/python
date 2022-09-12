#coding:utf-8
# 遍历
# stus = ["孙悟空","猪八戒","沙悟净","唐僧","二郎神","太上老君"]
# i = 0
# while i<len(stus):
#     print(stus[i])
#     i += 1

# for stu in stus:
#     print(stu)

# range():生成一个自然数序列，配合for循环来使用
# 起始位置(可以省略)，结束位置，步长(可以省略，默认是1)，左闭右开
r = range(5)
r = range(1,8,2)
r = range(9,1,-1)
print(list(r))