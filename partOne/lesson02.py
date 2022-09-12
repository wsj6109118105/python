#coding:utf-8
# input函数

# input函数会使程序停下，等待输入后再往后执行
# input会将输入存在变量中
# input 返回值永远是一个字符串
a = input("请输入用户名：")
if a == "admin":
    print("欢迎管理员！")