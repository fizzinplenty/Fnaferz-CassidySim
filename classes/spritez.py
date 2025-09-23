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
