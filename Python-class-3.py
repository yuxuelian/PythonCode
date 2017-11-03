#-*-coding:utf-8-*-

'''class  多继承'''

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#动物类
class Animal(object):
    pass

#哺乳动物
class Mammal(Animal):
    pass
#鸟
class Bird(Animal):
    pass

#狗
class Dog(Mammal,Runnable):
    pass

#蝙蝠
class Bat(Mammal,Flyable):
    pass
# 鹦鹉
class Parrot(Bird,Flyable):
    pass
 # 鸵鸟
class Ostrich(Bird,Flyable):
    pass


def main():
	d=Dog()
	d.run()

	b=Bat()
	b.fly()


if __name__ == '__main__':
	main()