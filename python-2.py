#-*- coding:utf-8 -*-
#�б�
name=["wangkaibo",123,123,1.3]
name2=["������",123,123,1.3]

#���뵽���
name.append("������")
#ɾ��ָ��λ��
name.insert(0,123)

name3=name+name2

#��name�ϲ���name2�б����ȥ
name2.extend(name)

#ɾ�����һ��
name.pop()

#��������ɾ��  ɾ����������ɾ����һ�γ��ֵ�,ֻɾһ��
name.remove(123)

#ָ��indexɾ��
del name[0]


#�б���Ƭ
name[0:-1]

name[::-1]

#����
name2[0]="kaibo"

if 123 in name2:
	print("��123")


#�ֵ�����,������js����


info1={"name":"wangkaibo","age":18}

print(info1["name"])
print(info1["age"])
