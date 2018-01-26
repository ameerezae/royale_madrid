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
        self.heroes = ['Wizard','giant','Musketeers','hunter','Barbarian','Archer','Knight','hog']
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
            if b.image == 'giant'or b.image == 'Knight' or b.image == 'hog' or b.image == 'Barbarian':
                if b.healthheroesUnarmed() == True:
                    b.moveplayer1Unarmed()
                    b.drawhero()
            else:
                if b.healthheroes() == True:
                    b.moveplayer1()
                    b.drawhero()




class player2():
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
        self.heroes = ['Wizard','giant','Musketeers','hunter','Barbarian','Archer','Knight','hog']
        self.heroes_push = []
        self.check = [1]
        self.replace1 = False
        self.replace2 = False
        self.replace3 = False
        self.replace4 = False
        self.X = False
        self.coordients = {'x':None,'y':None}
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
        self.blitheroes(str(self.heroes_push[0])+'Card',20,80)
        self.blitheroes(str(self.heroes_push[1])+'Card',105,80)
        self.blitheroes(str(self.heroes_push[2])+'Card',193,80)
        self.blitheroes(str(self.heroes_push[3])+'Card',282,80)
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
                self.blitheroes(str(self.heroes_push[0])+'Card',20,80)
            self.replace1 = True
        if L2 == 1:
            self.selecthero2 = True
            if len(self.heroes) == 4 and self.replace2 == False:
                self.heroes.append(self.heroes_push[1])
                self.heroes_push[1] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[1])+'Card',105,80)
            self.replace2 = True
        if R1 == 1:
            self.selecthero3 = True
            if len(self.heroes) == 4 and self.replace3 == False:
                self.heroes.append(self.heroes_push[2])
                self.heroes_push[2] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[2])+'Card',193,80)
            self.replace3 = True
        if R2 == 1:
            self.selecthero4 = True
            if len(self.heroes) == 4 and self.replace4 == False:
                self.heroes.append(self.heroes_push[3])
                self.heroes_push[3] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[3])+'Card',282,80)
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
            if b.image == 'giant'or b.image == 'Knight' or b.image == 'hog' or b.image == 'Barbarian':
                if b.healthheroesUnarmed() == True:
                    b.moveplayer2Unarmed()
                    b.drawhero()
            else:
                if b.healthheroes() == True:
                    b.moveplayer2()
                    b.drawhero()

class soldier():
    def __init__(self,x,y,pygame,surface,image):
        self.pygame = pygame
        self.surface = surface
        self.x = x
        self.y = y
        self.image = image
        self.Bullets = []
        self.health = {'Wizard':656,'Archer':300,'giant':1100,'Knight':1000,'hunter':576,'Barbarian':1100,'hog':944,'Musketeers':600}
    def drawhero(self):
        image = self.pygame.image.load(str(self.image)+'.jpg')
        self.surface.blit(image,(self.x,self.y))
    def moveplayer1(self):
        if 470 < self.x < 536:
            self.x += 1
        if 536 < self.x < 670:
            self.x -= 1
        if 670 < self.x < 753:
            self.x += 1
        if 753 < self.x < 865:
            self.x -=1
        if  260 < self.y < 680 and (self.x == 536 or self.x == 753):
            self.y -= 1

    def moveplayer2(self):
        if 65 < self.y < 325 and (self.x == 536 or self.x == 753):
            self.y += 1
        if 470 < self.x < 536:
            self.x += 1
        if 536 < self.x < 670:
            self.x -= 1
        if 670 < self.x < 753:
            self.x += 1
        if 753 < self.x < 865:
            self.x -=1
    def moveplayer2Unarmed(self):
        if 65 < self.y < 382 and (self.x == 536 or self.x == 753):
            self.y += 1
        if 470 < self.x < 536:
            self.x += 1
        if 536 < self.x < 670:
            self.x -= 1
        if 670 < self.x < 753:
            self.x += 1
        if 753 < self.x < 865:
            self.x -=1
    def moveplayer1Unarmed(self):
        if 470 < self.x < 536:
            self.x += 1
        if 536 < self.x < 670:
            self.x -= 1
        if 670 < self.x < 753:
            self.x += 1
        if 753 < self.x < 865:
            self.x -=1
        if  180 < self.y < 680 and (self.x == 536 or self.x == 753):
            self.y -= 1

    def healthheroes(self):
        if self.y == 260 and self.x == 536:
            if int(timer) %2 == 0 and self.health[str(self.image)] > 0 and tower3.healthtowers['tower3'] > 0:
                tower3.fireUpToDown()
                if self.image == 'Wizard':
                    tower3.healthtowers['tower3'] -= 4
                if self.image == 'Archer':
                    tower3.healthtowers['tower3'] -= 2
                if self.image == 'Musketters':
                    tower3.healthtowers['tower3'] -= 4
                if self.image == 'hunter':
                    tower3.healthtowers['tower3'] -= 4
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5

        if self.y == 260 and self.x == 753 and self.health[str(self.image)] > 0 and tower4.healthtowers['tower4'] > 0:
            if int(timer) %2 == 0:
                tower4.fireUpToDown()
                if self.image == 'Wizard':
                    tower4.healthtowers['tower4'] -= 4
                if self.image == 'Archer':
                    tower4.healthtowers['tower4'] -= 2
                if self.image == 'Musketters':
                    tower4.healthtowers['tower4'] -= 4
                if self.image == 'hunter':
                    tower4.healthtowers['tower4'] -= 4
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5
        if self.y == 325 and self.x == 536 and self.health[str(self.image)] > 0 and tower1.healthtowers['tower1'] > 0:
            if int(timer) %2 == 0 :
                tower1.fireDownToUp()
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Wizard':
                    tower1.healthtowers['tower1'] -= 4
                if self.image == 'Archer':
                    tower1.healthtowers['tower1'] -= 2
                if self.image == 'Musketters':
                    tower1.healthtowers['tower1'] -= 4
                if self.image == 'hunter':
                    tower1.healthtowers['tower1'] -= 4
                self.health[str(self.image)] -= 5

        elif self.y == 325 and self.x == 753 and self.health[str(self.image)] > 0 and tower2.healthtowers['tower2'] > 0:
            if int(timer) %2 == 0:
                tower2.fireDownToUp()
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Wizard':
                    tower3.healthtowers['tower2'] -= 4
                if self.image == 'Archer':
                    tower3.healthtowers['tower2'] -= 2
                if self.image == 'Musketters':
                    tower3.healthtowers['tower2'] -= 4
                if self.image == 'hunter':
                    tower3.healthtowers['tower2'] -= 4
                self.health[str(self.image)] -= 5
        if self.health[str(self.image)] <= 0:
            return False
        else:
            return True
    def healthheroesUnarmed(self):
        if self.y == 180 and self.x == 536:
            if int(timer) %2 == 0 and self.health[str(self.image)] > 0 and tower3.healthtowers['tower3'] > 0:
                tower3.fireforUnarmed(550,170)
                if self.image == 'Knight':
                    tower3.healthtowers['tower3'] -= 4
                if self.image == 'giant':
                    tower3.healthtowers['tower3'] -= 7
                if self.image == 'hog':
                    tower3.healthtowers['tower3'] -= 5
                if self.image == 'Barbarian':
                    tower3.healthtowers['tower3'] -= 6
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5
        if self.y == 180 and self.x == 753 and self.health[str(self.image)] > 0 and tower4.healthtowers['tower4'] > 0:
            if int(timer) %2 == 0:
                tower4.fireforUnarmed(765,170)
                if self.image == 'Knight':
                    tower4.healthtowers['tower4'] -= 4
                if self.image == 'giant':
                    tower4.healthtowers['tower4'] -= 7
                if self.image == 'hog':
                    tower4.healthtowers['tower4'] -= 5
                if self.image == 'Barbarian':
                    tower4.healthtowers['tower4'] -= 6
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5
        if self.y == 382 and self.x == 536 and self.health[str(self.image)] > 0 and tower1.healthtowers['tower1'] > 0:
            if int(timer) %2 == 0 :
                tower1.fireforUnarmed(550,410)
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Knight':
                    tower1.healthtowers['tower1'] -= 4
                if self.image == 'giant':
                    tower1.healthtowers['tower1'] -= 7
                if self.image == 'hog':
                    tower1.healthtowers['tower1'] -= 5
                if self.image == 'Barbarian':
                    tower1.healthtowers['tower1'] -= 6
                self.health[str(self.image)] -= 5

        elif self.y == 382 and self.x == 753 and self.health[str(self.image)] > 0 and tower2.healthtowers['tower2'] > 0:
            if int(timer) %2 == 0:
                tower2.fireforUnarmed(765,410)
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Knight':
                    tower2.healthtowers['tower2'] -= 4
                if self.image == 'giant':
                    tower2.healthtowers['tower2'] -= 7
                if self.image == 'hog':
                    tower2.healthtowers['tower2'] -= 5
                if self.image == 'Barbarian':
                    tower2.healthtowers['tower2'] -= 6
                self.health[str(self.image)] -= 5
        if self.health[str(self.image)] <= 0:
            return False
        else:
            return True
    def fireDownToUp(self):
        self.Bullets.append(Bullet(self.x,self.y,self.pygame,self.surface))
    def drawBulletDownToUp(self):
        for i in self.Bullets:
            i.moveToUp()
            i.drawbullets2()
    def fireUpToDown(self):
        self.Bullets.append(Bullet(self.x,self.y,self.pygame,self.surface))
    def drawBulletUpToDown(self):
        for i in self.Bullets:
            i.moveToDown()
            i.drawbullets1()
class tower():
    def __init__(self,x,y,pygame,surface):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.BulletsUpToDown = []
        self.BulletDownToUp = []
        self.healthtowers = {'tower1': 2786, 'tower2': 2786, 'tower3': 2786, 'tower4': 2786}
    def fireUpToDown(self):
        self.BulletsUpToDown.append(Bullet(self.x,self.y,self.pygame,self.surface))
    def drawUpToDown(self):
        for i in self.BulletsUpToDown:
            i.moveToDown()
            i.drawbulletUpToDown()
    def fireDownToUp(self):
        self.BulletDownToUp.append(Bullet(self.x,self.y,self.pygame,self.surface))
    def drawDownToUp(self):
        for i in self.BulletDownToUp:
            i.moveToUp()
            i.drawbulletDownToUp()
    def fireforUnarmed(self,x,y):
        bulletimage = self.pygame.image.load('bullet.png')
        self.surface.blit(bulletimage, (x, y))
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


windowwidth = 1280
windowheight = 605
window = pygame.display.set_mode((windowwidth,windowheight),pygame.FULLSCREEN)
battleScreen = pygame.image.load('battle Screen.jpg')
start_Screen = pygame.image.load('start_Screen.jpg')
timer_icon = pygame.image.load('timer_icon.png')
timer_box = pygame.image.load('timer_box.png')
player = player(windowwidth/2 ,windowheight/2 ,pygame ,window)
player2 = player2(windowwidth/2,windowheight/2,pygame,window)
start_sound = pygame.mixer.Sound('menu.ogg')
start_sound.play(-1)
bullet = pygame.image.load('bullet.png')
box = pygame.image.load('box.jpg')
box2 = pygame.image.load('box.jpg')
battle_sound = pygame.mixer.Sound('battle.ogg')
pygame.joystick.init()
tower1 = tower(548,420,pygame,window)
tower2 = tower(765,420,pygame,window)
tower3 = tower(548,148,pygame,window)
tower4 = tower(765,148,pygame,window)

timer = 100
dt = 0
def timer2():
    global timer,dt
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    blue = pygame.Color('red')

    timer -= dt
    if timer <= 0:
        timer = 0
    txt = font.render(str(round(timer, 1)), True, blue)
    window.blit(txt, (90, 30))
    dt = clock.tick(250) / 100

def draw_game():
    global hat ,x ,y
    window.blit(battleScreen,(0,0))
    window.blit(box,(934,475))
    window.blit(box2, (11, 67))
    window.blit(timer_icon, (10, 20))
    window.blit(timer_box, (80, 20))
    player.push()
    player2.push()
    player.click(L1,L2,R1,R2,X,x1,y1)
    player.drawsoldier()
    player2.click(L12,L22,R12,R22,X2,x2,y2)
    player2.drawsoldier()
    tower1.drawDownToUp()
    tower2.drawDownToUp()
    tower3.drawUpToDown()
    tower4.drawUpToDown()
start_battle = False
x1 = 640
y1= 395
x2 = 665
y2 = 273
while True:
    mouseState = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if 483 < mousepos[0] < 777 and 465 < mousepos[1] < 574 and  mouseState[0] == True:
                start_battle = True
                start_sound.stop()
                battle_sound.play(-1)
    joystuck_count = pygame.joystick.get_count()
    #for i in range(1):
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    hats = joystick.get_numhats()
    hat = joystick.get_hat(0)
    butttons = joystick.get_numbuttons()
    L1 = joystick.get_button(4)
    L2 = joystick.get_button(5)
    R1 = joystick.get_button(6)
    R2 = joystick.get_button(7)
    X = joystick.get_button(2)
    joystick = pygame.joystick.Joystick(1)
    joystick.init()
    hats2 = joystick.get_numhats()
    hat2 = joystick.get_hat(0)
    butttons2 = joystick.get_numbuttons()
    L12 = joystick.get_button(4)
    L22 = joystick.get_button(5)
    R12 = joystick.get_button(6)
    R22 = joystick.get_button(7)
    X2 = joystick.get_button(2)

    if start_battle == True:
        if hat[0] == 1:
            x1 += 5
        if hat[0] == -1:
            x1 -= 5
        if hat[1] == 1:
            y1 -= 5
        if hat[1] == -1 :
            y1 += 5
        if hat2[0] == 1:
            x2 += 5
        if hat2[0] == -1:
            x2 -= 5
        if hat2[1] == 1:
            y2 -= 5
        if hat2[1] == -1:
            y2 += 5

        draw_game()
        timer2()
        # print(tower2.healthtowers['tower2'])


        # print(mousepos)

    else:
        window.blit(start_Screen,(0,0))
    pygame.display.update()
