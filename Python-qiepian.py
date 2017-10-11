#-*-coding:utf-8-*-
#切片
list1=["1","2","3","4","5"]

print(list1)

#切0-3的元素
print(list1[0:3])
print(list1[1:4])
#切前2个
print(list1[:2])

#创建0-99的列表
list2=list(range(50))

#取前20个
print(list2[:20])

#取后20个
print(list2[-20:])

#11到20步长为2取
print(list2[10:20:2])

#步长为5取
print(list2[::5])

#复制list
print(list2[:])

#逆序
print(list1[-1::-1])

#tuple也是一种list  
#也可以切片 
#只是操作的结果仍是tuple
tuple1=(0, 1, 2, 3, 4, 5)

print(tuple1[:3])


#字符串也可以看成是一种list
#也可以切片

str1="wangkaibo王开波"
#逆序
print(str1[-1::-1])














