#-*- coding:utf-8 -*-

# i=1
# while i<=9:
# 	j=1
# 	while j<=i:
# 		print("%d*%d=%d\t"%(j,i,i*j)),
# 		j+=1
# 	print("")
# 	i+=1

#for 
name="wangkaibo"

for temp in name:
	print(temp)


strNum='100'


#
num=int(strNum)
print(num)
str1="====%d===="%(num)
print(str1)

num=100
#
strNum=str(num)

print(strNum)

#
print(strNum[0])


#
print(strNum[-1])

str2="====%s===="%(strNum)
print(str2)


#len 长度
print("len(strNum)=%d"%(len(strNum)))


#
str3="abcdefghijklmn"
print(str3)
#[0-5)
print(str3[0:5])

#0切到倒数第二
print(str3[0:-1])
#指定位置切到最后
print(str3[5:])
#指定步进
print(str3[0::5])
#字符串逆序
print(str3[-1::-1])
print(str3[::-1])