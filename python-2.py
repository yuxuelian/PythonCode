#-*- coding:utf-8 -*-
#列表
name=["wangkaibo",123,123,1.3]
name2=["王开波",123,123,1.3]

#插入到最后
name.append("王开波")
#删除指定位置
name.insert(0,123)

name3=name+name2

#将name合并到name2列表里边去
name2.extend(name)

#删除最后一个
name.pop()

#根据内容删除  删除从左往右删除第一次出现的,只删一次
name.remove(123)

#指定index删除
del name[0]


#列表切片
name[0:-1]

name[::-1]

#更新
name2[0]="kaibo"

if 123 in name2:
	print("有123")


#字典类型,类似于js对象


info1={"name":"wangkaibo","age":18}

print(info1["name"])
print(info1["age"])
