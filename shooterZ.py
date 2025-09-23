from init import *
import sys
import pygame, random, time
pygame.init()
screenY = 1080
screenX = 843
screen = pygame.display.set_mode((screenX,screenY))
running = True

#spritez
class sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_list = []
        self.sprites_list.append(pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/purplez/purple.png"))
        self.sprites_list.append(pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/purplez/purple1.png"))
        self.sprites_list.append(pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/purplez/purple2.png"))
        self.sprites_list.append(pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/purplez/purple3.png"))
        self.current_sprite = 0
        self.image = self.sprites_list[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self,speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites_list):
            self.current_sprite = 0
        self.image = self.sprites_list[int(self.current_sprite)]

sprites = pygame.sprite.Group()
porple = sprite(screenX/2,screenY/2)
sprites.add(porple)

#Images:
stickma = pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/cassidy.png").convert_alpha()
stickman = pygame.transform.scale(stickma,(950,903))
boolet = pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/boolet.png").convert_alpha()
Boolet = pygame.transform.scale(boolet, (100,100))
RPY = random.randint(0, 500)
RPX = random.randint(100, 700)
StickMan = pygame.transform.scale(stickman, (150, 150))
font = pygame.font.Font(None,40)
status = pygame.font.Font(None, 40)
bucks = pygame.font.Font(None,40)
timerfont = pygame.font.Font(None,40)
buttonlabel = pygame.font.Font(None,100)
greetingz = pygame.font.Font
shot = False

#button class:
class button():
    def __init__(self, buttonh, buttonw, buttonx, buttony, color):
        self.buttonw = buttonw
        self.buttonh = buttonh
        self.buttonx = buttonx
        self.buttony = buttony
        self.color = color
shopback = button(50,100, 35, 170, "red")
buttonlabelercolor = "white"
shop_init = False

#velocities:
velocity = 10
bullet_velocity = -10

#constants:
fazcoins = 0
status = ""
StickMan.set_colorkey((255,255,255))
changeX, changeY = 0, 0
stickmanX, stickmanY = screenX/2, screenY/2
bullet_posX, bullet_posY = 1001, 0
timer = 0
score = 0
clock = pygame.time.Clock()
running = True
fps = 120
time_between_frames = (1/fps)
target_velocity = 60
bullet_changeX = 0
bullet_changeY = 0
prev_time = pygame.time.get_ticks()


while running:
    now = pygame.time.get_ticks()
    dt = (now - prev_time)/1000
    now = prev_time
    timer = dt
    mouse_post = pygame.mouse.get_pos()
    mouse_pos = list(mouse_post)
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    mouse_status = pygame.mouse.get_pressed()


    offy = pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/8bitOffice.png")
    office = pygame.transform.scale(offy, (900, 900))
    screen.blit(office, (0, 0))


    purplegoy = pygame.image.load("/Users/fizzysoda/PycharmProjects/shooter/images/purpleguy.png").convert_alpha()
    purpleguy = pygame.transform.scale(purplegoy, (100, 100))
    screen.blit(purpleguy, (RPX, RPY))

    shopbackgroundd = pygame.draw.rect(screen, shopback.color,(shopback.buttonx, shopback.buttony, shopback.buttonw, shopback.buttonh))

    if 135 >= mouse_x >= 30 and 220 >= mouse_y >= 170:
        shopback.color = "purple"
        buttonlablercolor = "green"
        buttonlabeler = font.render("SHOP", True, buttonlabelercolor)
    else:
        shopback.color = "red"
        buttonlablercolor = "white"
        buttonlabeler = font.render("SHOP", True, buttonlabelercolor)

    scorer = font.render("Score: "+str(score),True,"red")
    statuser = font.render(f"Status: {status}",True, "green")
    buckler = font.render(f"Faz Coins: {str(fazcoins)}", True, "yellow")
    cooldown = font.render(f"Cooldown: {str(mouse_status)}", True, "pink")
    screen.blit(scorer,(20,50))
    screen.blit(statuser, (20,10))
    screen.blit(buckler, (20,90))
    screen.blit(cooldown, (20, 130))
    screen.blit(buttonlabeler,(45.5,182))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:

                changeY = -(velocity)
                changeX =  0

            elif event.key == pygame.K_s:
                changeY =  (velocity)
                changeX =  0


            elif event.key == pygame.K_a:
                changeX = -(velocity)
                changeY = 0

            elif event.key == pygame.K_d:
                changeX = (velocity)
                changeY =  0
            elif event.key == pygame.K_SPACE and not shot:
                bullet_posX, bullet_posY = stickmanX, stickmanY
                shot = True
                status = "shooting..."
                timer = dt = (now - prev_time)/1000
                bullet_posX, bullet_posY = stickmanX, stickmanY

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                changeY = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                changeX = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and 135 >= mouse_x >= 30 and 220 >= mouse_y >= 170:
                shop_init = True


    if shop_init == True:
        shop_tab = pygame.draw.rect(screen,"green",(200,200,screenX/2,screenY/2))

    if shot:
        bullet_changeY = bullet_velocity
        bullet_changeX = 0
        screen.blit(Boolet, (bullet_posX+30, bullet_posY))


    if (bullet_posX > 1000 or bullet_posX < 0) or (bullet_posY > 1000 or bullet_posY < 0):
        bullet_changeX, bullet_changeY = 0, 0
        screen.blit(Boolet, (bullet_posX+30, bullet_posY-85))
        shot = False
    elif (RPX + 40 >= bullet_posX >= RPX - 50) and (RPY + 50 >= bullet_posY >= RPY - 50):
        score += 100
        status = "hit!"
        fazcoins += 1
        RPY = random.randint(0, 500)
        RPX = random.randint(100, 700)

    if score > 2000:
        bullet_velocity = -20


    stickmanX += changeX
    stickmanY += changeY
    bullet_posX += bullet_changeX
    bullet_posY += bullet_changeY


    screen.blit(StickMan,(stickmanX,stickmanY))
    sprites.draw(screen)
    sprites.update(0.1)


    pygame.display.flip()

pygame.quit()



pygame.quit()


