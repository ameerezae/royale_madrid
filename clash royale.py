import pygame ,sys ,random
pygame.init()

class player():
    def __init__(self,x,y,pygame,surface):
        self.wizard = None
        self.musketeer = None
        self.giant = None
        self.hunter = None
        self.icewizard = None
        self.princess = None
        self.dart = None
        self.executioner = None
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.heroes = ['Wizard','giant','Musketeers','hunter','SpearGoblin','Archer','Dart goblin','Executioner']
        self.heroes_push = []
        self.check = [1]
        self.replace1 = False
        self.replace2 = False
        self.replace3 = False
        self.replace4 = False
        self.X = False
        self.soldiers = []
    def blitheroes(self,image,x,y):
        image = self.pygame.image.load(str(image)+'.jpg')
        self.surface.blit(image,(x,y))
    def push(self):
        if len(self.heroes)==8:
            hero1 = random.choice(self.heroes)
            self.heroes_push.append(hero1)
            self.heroes.remove(hero1)
            hero2 = random.choice(self.heroes)
            self.heroes_push.append(hero2)
            self.heroes.remove(hero2)
            hero3 = random.choice(self.heroes)
            self.heroes_push.append(hero3)
            self.heroes.remove(hero3)
            hero4 = random.choice(self.heroes)
            self.heroes_push.append(hero4)
            self.heroes.remove(hero4)
        self.blitheroes(str(self.heroes_push[0])+'Card',945,490)
        self.blitheroes(str(self.heroes_push[1])+'Card',1032,490)
        self.blitheroes(str(self.heroes_push[2])+'Card',1120,490)
        self.blitheroes(str(self.heroes_push[3])+'Card',1205 ,490)

    def click(self,L1,L2,R1,R2,X,x,y):
        if len(self.check) == 1:
            self.selecthero1 = False
            self.selecthero2 = False
            self.selecthero3 = False
            self.selecthero4 = False
        self.check.append(3)
        if L1 == 1:
            self.selecthero1 = True
            if len(self.heroes) == 4 and self.replace1 == False:
                self.heroes.append(self.heroes_push[0])
                self.heroes_push[0] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[0])+'Card',945,490)
            self.replace1 = True
        if L2 == 1:
            self.selecthero2 = True
            if len(self.heroes) == 4 and self.replace2 == False:
                self.heroes.append(self.heroes_push[1])
                self.heroes_push[1] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[1])+'Card',1032,490)
            self.replace2 = True
        if R1 == 1:
            self.selecthero3 = True
            if len(self.heroes) == 4 and self.replace3 == False:
                self.heroes.append(self.heroes_push[2])
                self.heroes_push[2] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[2])+'Card',1120,490)
            self.replace3 = True
        if R2 == 1:
            self.selecthero4 = True
            if len(self.heroes) == 4 and self.replace4 == False:
                self.heroes.append(self.heroes_push[3])
                self.heroes_push[3] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[3])+'Card',1205,490)
            self.replace4 = True
        if self.selecthero1 == True:
            self.pointer_position(x,y)
            if X == 1 and self.X == False:
                self.selecthero1 = False
                self.replace1 = False
                self.soldiers.append(soldier(x-17,y-20,self.pygame,self.surface,self.heroes[3]))

        if self.selecthero2 == True:
            self.pointer_position(x,y)
            if X == 1 and self.X == False:
                self.selecthero2 = False
                self.replace2 = False
                self.soldiers.append(soldier(x-17,y-20,self.pygame,self.surface,self.heroes[3]))
        if self.selecthero3 == True:
            self.pointer_position(x,y)
            if X == 1 and self.X == False:
                self.selecthero3 = False
                self.replace3 = False
                self.soldiers.append(soldier(x-17,y-20,self.pygame,self.surface,self.heroes[3]))
        if self.selecthero4 == True:
            self.pointer_position(x,y)
            if X == 1 and self.X == False:
                self.selecthero4 = False
                self.replace4 = False
                self.soldiers.append(soldier(x-17,y-20,self.pygame,self.surface,self.heroes[3]))


    def pointer_position(self,x,y):
        self.pygame.draw.circle(self.surface,(255,255,255),(x,y),5,0)
    def drawsoldier(self):
        for b in self.soldiers:
            if b.healthheroes() == True:
                b.moveplayer1()
                b.drawhero()

class Bullet():
    def __init__(self,x,y,pygame,surface):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.speed = 10
    def moveToUp(self):
        self.y -= self.speed
    def moveToDown(self):
        self.y += self.speed
    def drawbulletUpToDown(self):
        if self.y < 250:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage,(self.x,self.y))
    def drawbulletDownToUp(self):
        if self.y > 350:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage,(self.x,self.y))
    def drawbullets2(self):
        if self.y > 152:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))
    def drawbullets1(self):
        if self.y < 420:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))

