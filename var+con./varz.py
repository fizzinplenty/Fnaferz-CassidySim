shot = False
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
fps = 60
time_between_frames = (1/fps)
target_velocity = 60
bullet_changeX = 0
bullet_changeY = 0
prev_time = pygame.time.get_ticks()
