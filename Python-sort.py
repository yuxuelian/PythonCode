#-*-coding:utf-8-*-

#Python排序

#使用Python内置 sorted函数对list进行排序

list1=[1,23,234,1,123,2,34,456]
list1=sorted(list1)

print(list1)

#字符串排序
list2=['bob', 'about', 'Zoo', 'Credit']
print(sorted(list2))

#忽略字符串的大小写进行排序
print(sorted(list2,key=str.lower,reverse=False))



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]

L2 = sorted(L, key=by_name,reverse=False)
print(L2)

def by_score(t):
	return t[1]

L2 = sorted(L, key=by_score,reverse=True)
print(L2)





















