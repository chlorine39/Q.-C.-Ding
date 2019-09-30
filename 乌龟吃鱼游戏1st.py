import random as r

class Fish():
    def __init__(self):
        x=r.randint(0,10)
        y=r.randint(0,10)
        self.local=[x,y]

    def move(self):
        if r.randint(0,1):#判断上下移动或是左右移动
            self.local[0]=self.local[0]+r.choice([1,-1])
        else:
            self.local[1]=self.local[1]+r.choice([1,-1])
        #判断x轴是否越界
        if self.local[0]<0:
            self.local[0]=0-self.local[0]
        if self.local[0]>10:
            self.local[0]=10-(self.local[0]-10)
        #判断y轴是否越界
        if self.local[1]<0:
            self.local[1]=0-self.local[1]
        if self.local[1]>10:
            self.local[1]=10-(self.local[1]-10)
        return self.local


class Gui():
    def __init__(self):
        self.hp=100
        x=r.randint(0,10)
        y=r.randint(0,10)
        self.local=[x,y]

    def move(self):
        step=r.choice([1,2])#确定前进的步数
        if r.randint(0,1):#判断上下移动或是左右移动
            self.local[0]=self.local[0]+r.choice([1,-1,2,-2])
        else:
            self.local[1]=self.local[1]+r.choice([1,-1,2,-2])
        #判断x轴是否越界
        if self.local[0]<0:
            self.local[0]=0-self.local[0]
        if self.local[0]>10:
            self.local[0]=10-(self.local[0]-10)
        #判断y轴是否越界
        if self.local[1]<0:
            self.local[1]=0-self.local[1]
        if self.local[1]>10:
            self.local[1]=10-(self.local[1]-10)
        self.hp-=1
        return self.local

    def eat(self):
        self.hp+=20
        if self.hp>100:
            self.hp=100


def game():
    print('game start')
    turtle1=Gui()
    fishes=[]
    for i in range(10):
        fishes.append(Fish())
    times=0
    while True:
        times+=1
        print('第%d轮'%times)
        turtle1.move()
        for each in fishes:
            each.move()
            if each.local==turtle1.local:
                fishes.remove(each)
                turtle1.eat()
        if fishes==[] or turtle1.hp==0:
            print('游戏在第%d轮结束'%times)
            break


        
        


        
        

        
