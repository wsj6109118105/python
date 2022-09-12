#coding:utf-8
#if-else判断   while循环   break,continue
# 练习一：判断用户输入是奇数还是偶数
num = int(input("请输入一个整数："))
if num&1 == 1:
    print("输入是一个奇数。")
else:
    print("输入是一个偶数。")

# 练习二：判断一个年份是否是闰年
year = int(input("请输入一个年份："))
if year%400 == 0 :
    print(year,"是闰年。")
elif year%4==0 and year%100!=0 :
    print(year,"是闰年。")
else:
    print(year,"不是闰年。")

# 练习三：求100以内所有奇数之和
a = 1
sum = 0
while a<=100:
    if a&1 == 1:
        sum += a
    a+=1
a = 1
sum = 0
while a<100:
    sum += a
    a += 2
print("和为：",sum)

# 练习4：求100以内7的倍数之和以及个数
a = 7
sum = 0
num = 0
while a<100:
    sum += a
    num += 1
    a += 7
print("和为：",sum,"总共有：",num)

# 练习5：水仙花数：n(n>=3)位数，每个位的n次幂之和等于这个数，求1000以内的水仙花数
a = 100
while a<1000:
    bai = a//100
    shi = (a%100)//10
    ge = a%10
    if bai**3+shi**3+ge**3==a:
        print(a,"是一个水仙花数")
    a += 1

# break
a = 1
while a<100:
    print(a)
    if a == 50:
        break
    a += 1

# continue
a = 0
while a<100:
    a += 1
    if a&1 == 0:
        continue
    print(a)
    