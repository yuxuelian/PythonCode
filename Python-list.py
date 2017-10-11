#-*- coding:utf-8 -*-
list1=["aaa","bbb","ccc"]

#空的list
emptyList=[]

#计算list长度
length=len(list1)

#遍历list
for temp in list1:
	print(temp)

#插入list
list1.insert(1,"iii")
list1.append('append')
print(list1)

#删除list末尾的元素
list1.pop()
print(list1)

#删除指定位置的元素
del list1[2]
print(list1)

#修改指定位置的值
list1[0]="update"
print(list1)

# 生成0-19的 list
list2=list(range(20))
print(list2)

#元组 tuple  元组一旦被定义,就不能修改,,指向不能改变
classmates=('123','123asda','qweqwe')
print(classmates)

#空元组
emptyMeta=()
print(emptyMeta)

#元组中只有一个元素的时候也要加  , 号
singMeta=(1,)
print(singMeta)

#遍历元组
for temp in classmates:
	print(temp)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]


#打印Apple
print(L[0][0])
#打印Python
print(L[1][1])
#打印Lisa
print(L[2][2])


#条件判断
age=3
if age>3:
	print("age>3")

elif age==3:
	print("age==3")
else:
	print("age<3")

#字典 dict
d={'aaa':99,"name":'王开波'}
print(d['name'])
print(d['aaa'])

print("name是否在d中")
print('name' in d)


#set集合  无序,不可重复
s=set(list(range(10)))
print(s)

#增加 key
s.add(123)
print(s)

#删除key
s.remove(5)
print(s)

s2=set([6,7,8,9,10,11,23,434])
print(s2)

#交集
print("交集")
s3= s&s2
print(s3)

#并集
print("并集")
s4=s|s2
print(s4)

#字符串是不可变对象
a="abc"
print(a)


#replace并没有改变原来的'abc'字符串
#而是通过方法的处理结果是
#重新创建了'Abc'对象进行了返回
b=a.replace('a','A')
print(b)






#求1-100的和
i=1;
res=0;
while i<=100:
	res+=i
	i+=1
print("计算结果是:%d"%(res))



