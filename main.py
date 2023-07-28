import pygame
import random
pygame.init()
def spanzuratoare():
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Hangman 2.0")
    # fonts
    fontt = pygame.font.SysFont('comicsans', 40)

    secret = "andrei"
    # poze
    images = []
    for i in range(7):
        images.append(pygame.image.load("hangman" + str(i) + ".png"))
    # variabile
    hs = 0
    ok = 0
    # litere
    x = []
    y = []
    x1 = 100
    y1 = 400
    r = []
    t = 0
    ko = 0
    replay = pygame.Rect(300, 350, 99, 30)
    quitt = pygame.Rect(400, 350, 99, 30)
    for i in range(26):
        if i <= 12:
            x.append(x1 + i * 60)
        else:
            x.append(x1 + (i - 13) * 60)
        if i > 12:
            y.append(y1 + 70)
        else:
            y.append(y1)
        r.append(True)
    alf = "abcdefghijklmnopqrstuvwxyz"
    displayword = []
    for i in range(len(secret)):
        displayword.append("_")
    # gameloop
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        screen.fill((0, 20, 0))
        for i in range(26):
            if r[i] == True:
                pygame.draw.circle(screen, (200, 200, 200), (x[i], y[i]), 30, 3)
                text = fontt.render(chr(97 + i), 1, (250, 250, 250))
                screen.blit(text, (x[i] - 10, y[i] - 12))
        screen.blit(images[hs], (150, 100))
        textt = fontt.render(str(displayword), 1, (250, 250, 250))
        screen.blit(textt, (500, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 300 and pos[0] <= 399 and pos[1] > 350 and pos[1] < 380 and ko == 1 and w == True:
                    w = False
                    for i in range(26):
                        r[i] = True
                if pos[0] >= 400 and pos[0] <= 499 and pos[1] > 350 and pos[1] < 380 and ko == 1 and w == True:
                    run = False
                for i in range(26):
                    if r[i] == True:
                        if abs(pos[0] - x[i]) * abs(pos[0] - x[i]) + abs(pos[1] - y[i]) * abs(pos[1] - y[i]) <= 900:
                            l = alf[i]
                            # print(l)
                            k = 0
                            for j in range(len(secret)):
                                if secret[j] == l:
                                    k = k + 1
                                    t = t + 1
                                    displayword[j] = secret[j]
                            r[i] = False
                            if k == 0:
                                hs = hs + 1
                                if hs == 6:
                                    ko = 1
        if t == len(secret):
            for i in range(26):
                r[i] = False
                textu = fontt.render("BRAVO", 1, (250, 250, 250))
                screen.blit(textu, (400, 300))
        if ko == 1:
            textttt = fontt.render(
                chr(71) + chr(65) + chr(77) + chr(69) + chr(32) + chr(79) + chr(86) + chr(69) + chr(82), 1,
                (250, 250, 250))
            screen.blit(textttt, (400, 300))
            w = True
            for i in range(26):
                r[i] = False
                if w == True:
                    pygame.draw.rect(screen, (0, 0, 0), replay)
                    teextttt = fontt.render(chr(82) + chr(101) + chr(112) + chr(108) + chr(97) + chr(121), 1,
                                            (250, 250, 250))
                    screen.blit(teextttt, (300, 350))
                    pygame.draw.rect(screen, (0, 0, 0), quitt)
                    teeextttt = fontt.render(chr(81) + chr(117) + chr(105) + chr(116), 1, (250, 250, 250))
                    screen.blit(teeextttt, (400, 350))

        pygame.display.update()
    pygame.quit()
def plm():
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("0 si X")

    player = pygame.Rect(100, 100, 450, 450)
    replay = pygame.Rect(700, 100, 100, 30)
    images = []
    images.append(pygame.image.load("circl.png"))
    images.append(pygame.image.load("letter-x (1).png"))
    fontt = pygame.font.SysFont('comicsans', 40)

    win = 1

    rrun = True
    while rrun:
        fontt = pygame.font.SysFont('comicsans', 40)
        k = 1
        xc = 0
        ok = -1
        okk = -1
        okkk = -1
        okkkk = -1
        okkkkk = -1
        okkkkkk = -1
        okkkkkkk = -1
        okkkkkkkk = -1
        okkkkkkkkk = -1
        px = 0
        p1 = 0
        p2 = 0
        qw = 0
        er = 0
        v = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        r = [True, True, True, True, True, True, True, True, True]
        FPS = 60
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            screen.fill((200, 180, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if win == 0:
                        pygame.draw.rect(screen, (0, 0, 0), player, 3)
                        pygame.draw.aaline(screen, (0, 0, 0), (250, 100), (250, 550))
                        pygame.draw.aaline(screen, (0, 0, 0), (400, 100), (400, 550))
                        pygame.draw.aaline(screen, (0, 0, 0), (100, 250), (550, 250))
                        pygame.draw.aaline(screen, (0, 0, 0), (100, 250), (550, 250))
                        pygame.draw.aaline(screen, (0, 0, 0), (100, 400), (550, 400))
                        for i in range(9):
                            v[i] = 0
                            r[i] = True
                            k = 1
                        win = 1
                    if pos[0] > 100 and pos[0] < 250 and pos[1] > 100 and pos[1] < 250 and k % 2 == 1 and r[0] == True:
                        ok = 0
                        v[0] = 1
                        r[0] = False
                        k = k + 1
                    if pos[0] > 250 and pos[0] < 400 and pos[1] > 100 and pos[1] < 250 and k % 2 == 1 and r[1] == True:
                        okk = 1
                        v[1] = 1
                        r[1] = False
                        k = k + 1
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 100 and pos[1] < 250 and k % 2 == 1 and r[2] == True:
                        okkk = 2
                        v[2] = 1
                        r[2] = False
                        k = k + 1
                    if pos[0] > 100 and pos[0] < 250 and pos[1] > 250 and pos[1] < 400 and k % 2 == 1 and r[3] == True:
                        okkkk = 3
                        v[3] = 1
                        r[3] = False
                        k = k + 1
                    if pos[0] > 250 and pos[0] < 400 and pos[1] > 250 and pos[1] < 400 and k % 2 == 1 and r[4] == True:
                        okkkkk = 4
                        v[4] = 1
                        r[4] = False
                        k = k + 1
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 250 and pos[1] < 400 and k % 2 == 1 and r[5] == True:
                        okkkkkk = 5
                        v[5] = 1
                        r[5] = False
                        k = k + 1
                    if pos[0] > 100 and pos[0] < 250 and pos[1] > 400 and pos[1] < 550 and k % 2 == 1 and r[6] == True:
                        okkkkkkk = 6
                        v[6] = 1
                        r[6] = False
                        k = k + 1
                    if pos[0] > 250 and pos[0] < 400 and pos[1] > 400 and pos[1] < 550 and k % 2 == 1 and r[7] == True:
                        okkkkkkkk = 7
                        v[7] = 1
                        r[7] = False
                        k = k + 1
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 400 and pos[1] < 550 and k % 2 == 1 and r[8] == True:
                        okkkkkkkkk = 8
                        v[8] = 1
                        r[8] = False
                        k = k + 1

                    if pos[0] > 100 and pos[0] < 250 and pos[1] > 100 and pos[1] < 250 and k % 2 == 0 and r[0] == True:
                        ok = 0
                        v[0] = 2
                        r[0] = False
                        k = k + 1
                    if pos[0] > 250 and pos[0] < 400 and pos[1] > 100 and pos[1] < 250 and k % 2 == 0 and r[1] == True:
                        okk = 1
                        v[1] = 2
                        r[1] = False
                        k = k + 1
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 100 and pos[1] < 250 and k % 2 == 0 and r[2] == True:
                        okkk = 2
                        v[2] = 2
                        r[2] = False
                        k = k + 1
                    if pos[0] > 100 and pos[0] < 250 and pos[1] > 250 and pos[1] < 400 and k % 2 == 0 and r[3] == True:
                        okkkk = 3
                        v[3] = 2
                        r[3] = False
                        k = k + 1
                    if pos[0] > 250 and pos[0] < 400 and pos[1] > 250 and pos[1] < 400 and k % 2 == 0 and r[4] == True:
                        okkkkk = 4
                        v[4] = 2
                        r[4] = False
                        k = k + 1
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 250 and pos[1] < 400 and k % 2 == 0 and r[5] == True:
                        okkkkkk = 5
                        v[5] = 2
                        r[5] = False
                        k = k + 1
                    if pos[0] > 100 and pos[0] < 250 and pos[1] > 400 and pos[1] < 550 and k % 2 == 0 and r[6] == True:
                        okkkkkkk = 6
                        v[6] = 2
                        r[6] = False
                        k = k + 1
                    if pos[0] > 250 and pos[0] < 400 and pos[1] > 400 and pos[1] < 550 and k % 2 == 0 and r[7] == True:
                        okkkkkkkk = 7
                        v[7] = 2
                        r[7] = False
                        k = k + 1
                    if pos[0] > 400 and pos[0] < 550 and pos[1] > 400 and pos[1] < 550 and k % 2 == 0 and r[8] == True:
                        okkkkkkkkk = 8
                        v[8] = 2
                        r[8] = False
                        k = k + 1
            for i in range(9):
                q = i % 3
                w = int(i / 3)
                if v[i] == 1:
                    screen.blit(images[0], (110 + q * 150, 110 + w * 150))
                if v[i] == 2:
                    screen.blit(images[1], (110 + q * 150, 110 + w * 150))
            if v[0] == v[3] and v[0] == v[6] and v[0] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (175, 100), (175, 550))
                for i in range(9):
                    r[i] = False
                if v[0] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p2 = er + 1
                win = 0
            elif v[0] == v[4] and v[0] == v[8] and v[0] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (100, 100), (550, 550))
                for i in range(9):
                    r[i] = False
                if v[0] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                win = 0
            elif v[1] == v[4] and v[1] == v[7] and v[1] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (325, 100), (325, 550))
                for i in range(9):
                    r[i] = False
                if v[1] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                win = 0
            elif v[1] == v[0] and v[1] == v[2] and v[1] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (100, 175), (550, 175))
                for i in range(9):
                    r[i] = False
                if v[0] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                win = 0
            elif v[3] == v[4] and v[4] == v[5] and v[3] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (100, 325), (550, 325))
                for i in range(9):
                    r[i] = False
                if v[3] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                win = 0
            elif v[6] == v[7] and v[7] == v[8] and v[6] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (100, 475), (550, 475))
                for i in range(9):
                    r[i] = False
                if v[6] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p1 += 1
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p2 += 1
                win = 0
            elif v[2] == v[5] and v[8] == v[2] and v[2] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (475, 100), (475, 550))
                for i in range(9):
                    r[i] = False
                if v[2] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p1 += 1
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p2 += 1
                win = 0
            elif v[6] == v[4] and v[4] == v[2] and v[2] != 0:
                pygame.draw.aaline(screen, (0, 0, 255), (100, 550), (550, 100))
                for i in range(9):
                    r[i] = False
                if v[6] == 1:
                    text = fontt.render("player 1 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p1 += 1
                else:
                    text = fontt.render("player 2 wins", 1, (250, 250, 250))
                    screen.blit(text, (570, 125))
                    p2 += 1
                win = 0
            elif k == 10:
                pygame.draw.rect(screen, (0, 0, 0), player, 3)
                pygame.draw.aaline(screen, (0, 0, 0), (250, 100), (250, 550))
                pygame.draw.aaline(screen, (0, 0, 0), (400, 100), (400, 550))
                pygame.draw.aaline(screen, (0, 0, 0), (100, 250), (550, 250))
                pygame.draw.aaline(screen, (0, 0, 0), (100, 250), (550, 250))
                pygame.draw.aaline(screen, (0, 0, 0), (100, 400), (550, 400))
                for i in range(9):
                    v[i] = 0
                    r[i] = True
                    k = 1
                win = 1
            if win == 0:
                pygame.draw.rect(screen, (0, 0, 0), replay)
                text = fontt.render("Replay", 1, (250, 250, 250))
                screen.blit(text, (700, 100))
            pygame.draw.rect(screen, (0, 0, 0), player, 3)
            pygame.draw.aaline(screen, (0, 0, 0), (250, 100), (250, 550))
            pygame.draw.aaline(screen, (0, 0, 0), (400, 100), (400, 550))
            pygame.draw.aaline(screen, (0, 0, 0), (100, 250), (550, 250))
            pygame.draw.aaline(screen, (0, 0, 0), (100, 250), (550, 250))
            pygame.draw.aaline(screen, (0, 0, 0), (100, 400), (550, 400))
            pygame.display.update()
        rrun = False

        pygame.quit()

def shooter():
    def joc2():
        imagesleft = []
        for i in range(9):
            imagesleft.append(pygame.image.load("L" + str(i + 1) + ".png"))

        imagesright = []
        for i in range(9):
            imagesright.append(pygame.image.load("R" + str(i + 1) + ".png"))
        imagesleftt = []
        for i in range(9):
            imagesleft.append(pygame.image.load("L" + str(i + 1) + ".png"))

        imagesrightt = []
        for i in range(9):
            imagesright.append(pygame.image.load("R" + str(i + 1) + ".png"))

        bg = pygame.image.load("bg.jpg")
        chr = pygame.image.load("standing.png")
        chrr = pygame.image.load("standing.png")

        cloc = pygame.time.Clock()
        screen = pygame.display.set_mode((500, 480))
        pygame.display.set_caption("gogu")

        class player(object):
            def __init__(self, x, y, latime, inaltime):
                self.x = x
                self.y = y
                self.inaltime = inaltime
                self.latime = latime
                self.v = 5
                self.isJump = False
                self.JumpCount = 10
                self.right = False
                self.left = False
                self.walk = 0
                self.standing = True

            def draaw(self, screen):

                if self.walk + 1 >= 27:
                    self.walk = 0
                if not (self.standing):
                    if self.left:
                        screen.blit(imagesleft[self.walk // 3], (self.x, self.y))
                        self.walk += 1
                    elif self.right:
                        screen.blit(imagesright[self.walk // 3], (self.x, self.y))
                        self.walk += 1
                else:
                    if self.left:
                        screen.blit(imagesleft[0], (self.x, self.y))
                    elif self.right:
                        screen.blit(imagesright[0], (self.x, self.y))

        class proiectile(object):
            def __init__(self, x, y, radius, color, facing):
                self.x = x
                self.y = y
                self.radius = radius
                self.color = color
                self.facing = facing
                self.v = 8 * facing

            def draw(self):
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        def redrawwindow():
            global walk, patrat2
            screen.blit(bg, (0, 0))

            man.draaw(screen)
            mann.draaw(screen)
            pygame.draw.rect(screen, (255, 0, 0), patrat3)
            pygame.draw.rect(screen, (0, 255, 0), patrat4)
            pygame.draw.rect(screen, (255, 0, 0), patrat5)
            pygame.draw.rect(screen, (0, 255, 0), patrat6)
            for ball in bullets:
                ball.draw()
            for bal in bullet:
                bal.draw()
            if man.left == False and man.right == False:
                screen.blit(chr, (man.x, man.y))
            if mann.left == False and mann.right == False:
                screen.blit(chr, (mann.x, mann.y))
            if qw > 0 and qwe <= 0:
                text = fontt.render("player 1 wins", 1, (0, 0, 0))
                screen.blit(text, (200, 25))
            if qw <= 0 and qwe > 0:
                text = fontt.render("player 2 wins", 1, (0, 0, 0))
                screen.blit(text, (200, 25))
            pygame.display.update()

        man = player(300, 410, 64, 64)
        mann = player(350, 410, 64, 64)
        bullets = []
        bullet = []
        q = 0
        k = 0
        y = 0
        run = True
        while run:

            qwe = 45 - k * 5
            patrat4 = pygame.Rect(man.x + 20, man.y, qwe, 10)
            patrat3 = pygame.Rect(man.x + 20, man.y, 45, 10)
            qw = 45 - y * 5
            patrat6 = pygame.Rect(mann.x + 20, mann.y, qw, 10)
            patrat5 = pygame.Rect(mann.x + 20, mann.y, 45, 10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            cloc.tick(27)
            for ball in bullets:
                if ball.x < 500 and ball.x > 0:
                    ball.x += ball.v
                else:
                    bullets.pop(bullets.index(ball))
                if ball.x > mann.x + 20 and ball.x < mann.x + 30 and ball.y > mann.y and ball.y < mann.y + 54 and qwe > 0:
                    y = y + 1
                    bullets.pop(bullets.index(ball))

            for bal in bullet:
                if bal.x < 500 and bal.x > 0:
                    bal.x += bal.v
                else:
                    bullet.pop(bullet.index(bal))
                if bal.x > man.x + 20 and bal.x < man.x + 30 and bal.y > man.y and bal.y < man.y + 54 and qwe > 0:
                    k = k + 1
                    bullet.pop(bullet.index(bal))
            keys = pygame.key.get_pressed()
            if qw > 0 and qwe > 0:
                if keys[pygame.K_SPACE]:
                    if len(bullets) < 5:
                        if man.left:
                            bullets.append(proiectile(man.x + 32, man.y + 32, 5, (0, 0, 255), -1))

                        if man.right:
                            bullets.append(proiectile(man.x + 32, man.y + 32, 5, (0, 0, 255), 1))
                if keys[pygame.K_x]:
                    if len(bullet) < 5:
                        if mann.left:
                            bullet.append(proiectile(mann.x + 32, mann.y + 32, 5, (0, 0, 255), -1))

                        if mann.right:
                            bullet.append(proiectile(mann.x + 32, mann.y + 32, 5, (0, 0, 255), 1))
                if keys[pygame.K_LEFT] and man.x > -10:
                    man.x -= man.v
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT] and man.x < 450:
                    man.x += man.v
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walk = 0
                if not (man.isJump):
                    if keys[pygame.K_DOWN] and man.y < 400:
                        man.y += man.v
                    if keys[pygame.K_UP]:
                        man.isJump = True
                    man.y = 400
                else:
                    if man.JumpCount > -10:
                        man.y -= int((man.JumpCount * abs(man.JumpCount)) / 2)
                        man.JumpCount -= 1
                    else:
                        man.isJump = False
                        man.JumpCount = 10

                if keys[pygame.K_a] and mann.x > -10:
                    mann.x -= mann.v
                    mann.left = True
                    mann.right = False
                    mann.standing = False
                elif keys[pygame.K_d] and mann.x < 450:
                    mann.x += mann.v
                    mann.right = True
                    mann.left = False
                    mann.standing = False
                else:
                    mann.standing = True
                    mann.walk = 0
                if not (mann.isJump):
                    if keys[pygame.K_s] and mann.y < 400:
                        mann.y += mann.v
                    if keys[pygame.K_w]:
                        mann.isJump = True
                    mann.y = 400
                else:
                    if mann.JumpCount > -10:
                        mann.y -= int((mann.JumpCount * abs(mann.JumpCount)) / 2)
                        mann.JumpCount -= 1
                    else:
                        mann.isJump = False
                        mann.JumpCount = 10
            else:
                if keys[pygame.K_r]:
                    qwe = 45
                    qw = 45
                    k = 0
                    y = 0

            redrawwindow()

    def joc1():

        imagesleft = []
        for i in range(9):
            imagesleft.append(pygame.image.load("L" + str(i + 1) + ".png"))

        imagesright = []
        for i in range(9):
            imagesright.append(pygame.image.load("R" + str(i + 1) + ".png"))

        bg = pygame.image.load("bg.jpg")
        chr = pygame.image.load("standing.png")

        class player(object):
            def __init__(self, x, y, latime, inaltime):
                self.x = x
                self.y = y
                self.inaltime = inaltime
                self.latime = latime
                self.v = 5
                self.isJump = False
                self.JumpCount = 10
                self.right = False
                self.left = False
                self.walk = 0
                self.standing = True

            def draaw(self, screen):

                if self.walk + 1 >= 27:
                    self.walk = 0
                if not (self.standing):
                    if self.left:
                        screen.blit(imagesleft[self.walk // 3], (self.x, self.y))
                        self.walk += 1
                    elif self.right:
                        screen.blit(imagesright[self.walk // 3], (self.x, self.y))
                        self.walk += 1
                else:
                    if self.left:
                        screen.blit(imagesleft[0], (self.x, self.y))
                    elif self.right:
                        screen.blit(imagesright[0], (self.x, self.y))

        class enemy(object):
            walkright = []
            for i in range(11):
                walkright.append(pygame.image.load("R" + str(i + 1) + "E.png"))
            walkleft = []
            for i in range(11):
                walkleft.append(pygame.image.load("L" + str(i + 1) + "E.png"))

            def __init__(self, x, y, inaltime, latime, sf):
                self.x = x
                self.y = y
                self.ok = 0
                self.inaltime = inaltime
                self.latime = latime
                self.sf = sf
                self.path = [1, self.sf]
                self.walcount = 0
                self.v = 3
                self.k = 0

            def draw(self, screen):
                if qw > 1:
                    self.move()
                    if self.walcount + 1 >= 33:
                        self.walcount = 0
                    if self.v > 0:
                        screen.blit(self.walkright[self.walcount // 3], (self.x, self.y))
                        self.walcount += 1
                    else:
                        screen.blit(self.walkleft[self.walcount // 3], (self.x, self.y))
                        self.walcount += 1
                else:
                    screen.blit(self.walkleft[1], (self.x, self.y))

            def move(self):
                if self.v > 0:
                    if self.x + self.v < self.path[1]:
                        self.x += self.v
                    elif self.x + self.v >= self.path[1]:
                        self.v = self.v * -1
                        self.walcount = 0
                else:
                    if self.x - self.v > self.path[0]:
                        self.x += self.v
                    else:
                        self.v = self.v * -1
                        self.walcount = 0
                self.patrat2 = pygame.Rect(self.x + 20, self.y, 30, 54)
                self.patrat3 = pygame.Rect(self.x + 20, self.y, 40, 10)

        class proiectile(object):
            def __init__(self, x, y, radius, color, facing):
                self.x = x
                self.y = y
                self.radius = radius
                self.color = color
                self.facing = facing
                self.v = 8 * facing

            def draw(self):
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        def redrawwindow():
            global walk, patrat2
            screen.blit(bg, (0, 0))
            man.draaw(screen)
            for ball in bullets:
                ball.draw()

            en.draw(screen)
            pygame.draw.rect(screen, (255, 0, 0), en.patrat3)
            pygame.draw.rect(screen, (0, 255, 0), patrat4)
            pygame.draw.rect(screen, (255, 255, 255), vchen, 3)
            if qw >= 1:
                pygame.draw.rect(screen, (255, 0, 0), vchen2)
            else:
                textt = fontt.render("GAME OVER", 1, (0, 0, 0))
                screen.blit(textt, (200, 250))
            if man.left == False and man.right == False:
                screen.blit(chr, (man.x, man.y))
            text = fontt.render(str(ass * 100), 1, (0, 0, 0))
            screen.blit(text, (400, 25))
            pygame.display.update()

        man = player(300, 410, 64, 64)
        en = enemy(150, 410, 64, 64, 450)
        bullets = []
        q = 0
        k = 0
        ass = 0
        p = 8
        run = True
        while run:
            cloc.tick(27)
            # patrat1 = pygame.Rect(man.x + 15, man.y + 12, 35, 54)
            qwe = 45 - k * 5
            patrat4 = pygame.Rect(en.x + 20, en.y, qwe, 10)
            vchen = pygame.Rect(15, 12, 100, 10)
            qw = 96 - int(q * p / 10)
            vchen2 = pygame.Rect(18, 15, qw, 4)
            if qwe == 0 and qw > 0:
                qwe = 45
                en.v = en.v + 5
                k = 0
                p += 2
                en.x = random.randint(1, 400)
                en.y = 410
            if abs(man.x + 12 - en.x) < 30 and abs(man.y + 25 - en.y) < 54 and qwe > 0:
                q = q + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for ball in bullets:
                if ball.x < 500 and ball.x > 0:
                    ball.x += ball.v
                else:
                    bullets.pop(bullets.index(ball))
                if ball.x > en.x + 20 and ball.x < en.x + 30 and ball.y > en.y and ball.y < en.y + 54 and qwe > 0:
                    ass = ass + 1
                    k = k + 1
                    bullets.pop(bullets.index(ball))

            keys = pygame.key.get_pressed()
            if qw >= 1:
                if keys[pygame.K_SPACE]:
                    if len(bullets) < 5:
                        if man.left:
                            bullets.append(proiectile(man.x + 32, man.y + 32, 5, (0, 0, 255), -1))

                        if man.right:
                            bullets.append(proiectile(man.x + 32, man.y + 32, 5, (0, 0, 255), 1))
                if keys[pygame.K_LEFT] and man.x > -10:
                    man.x -= man.v
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT] and man.x < 450:
                    man.x += man.v
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walk = 0
                if not (man.isJump):
                    if keys[pygame.K_DOWN] and man.y < 400:
                        man.y += man.v
                    if keys[pygame.K_UP]:
                        man.isJump = True
                    man.y = 400
                else:
                    if man.JumpCount > -10:
                        man.y -= int((man.JumpCount * abs(man.JumpCount)) / 2)
                        man.JumpCount -= 1
                    else:
                        man.isJump = False
                        man.JumpCount = 10
            else:
                if keys[pygame.K_CAPSLOCK]:
                    qw = 96
                    q = 0
                    en.v = 3
                    qwe = 45
                    p = 8
                    ass = 0
            redrawwindow()

    cloc = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 480))
    pygame.display.set_caption("Un fel de shooter")
    fontt = pygame.font.SysFont('comicsans', 40)
    fonttt = pygame.font.SysFont('comicsans', 30)
    ui = 0
    run = True
    patratel = pygame.Rect(100, 320, 100, 70)
    patratel2 = pygame.Rect(300, 320, 100, 70)
    while run:
        screen.fill((80, 80, 90))
        pygame.draw.rect(screen, (60, 80, 100), patratel)
        pygame.draw.rect(screen, (155, 155, 155), patratel2)
        textt = fonttt.render("SINGLE", 1, (0, 0, 0))
        texttT = fonttt.render("PLAYER", 1, (0, 0, 0))
        screen.blit(textt, (105, 330))
        screen.blit(texttT, (105, 350))
        textt = fonttt.render("MULTI", 1, (0, 0, 0))
        texttT = fonttt.render("PLAYER", 1, (0, 0, 0))
        screen.blit(textt, (305, 330))
        screen.blit(texttT, (305, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0] > 100 and pos[0] < 200 and pos[1] > 320 and pos[1] < 390 and ui == 0:
                    ui = 1
                if pos[0] > 300 and pos[0] < 500 and pos[1] > 320 and pos[1] < 390 and ui == 0:
                    ui = 2
        if ui == 1:
            joc1()
        if ui == 2:
            joc2()
        pygame.display.update()
def paint():
    pygame.init()
    latime = 900
    l = 1 / 8 * latime
    screen = pygame.display.set_mode((latime, latime))
    pygame.display.set_caption("Un fel de paint")
    fontt = pygame.font.SysFont('comicsans', 40)
    fonttt = pygame.font.SysFont('comicsans', 20)
    traseuu = 1
    FPS = 60
    lat = 20
    posi = []
    print(len(posi))
    ok = 0
    rtt = 0
    k = 0
    galben = pygame.Rect(0, 3 / 4 * latime, l, l)
    albastru = pygame.Rect(l, 3 / 4 * latime, l, l)
    alb = pygame.Rect(0, 3 / 4 * latime + l, l, l)
    verde = pygame.Rect(l, 3 / 4 * latime + l, l, l)
    rosu = pygame.Rect(2 * l, 3 / 4 * latime, l, l)
    mov = pygame.Rect(2 * l, 3 / 4 * latime + l, l, l)
    traseu = pygame.Rect(700, 3 / 4 * latime, 199, 1 / 8 * latime)
    nou = pygame.Rect(700, 3 / 4 * latime + 1 / 8 * latime, 199, 1 / 8 * latime)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0] <= l and pos[1] >= 3 / 4 * latime and pos[1] < 3 / 4 * latime + 90:
                    ok = 1
                if pos[0] > l and pos[0] <= 2 * l and pos[1] >= 3 / 4 * latime and pos[1] < 3 / 4 * latime + l:
                    ok = 0
                if pos[0] <= l and pos[1] >= 3 / 4 * latime + l and pos[1] < 3 / 4 * latime + 2 * l:
                    ok = 2
                if pos[0] > l and pos[0] <= 2 * l and pos[1] >= 3 / 4 * latime + l and pos[1] <= 3 / 4 * latime + 2 * l:
                    ok = 3
                if pos[0] > 2 * l and pos[0] <= 3 * l and pos[1] >= 3 / 4 * latime and pos[1] <= 3 / 4 * latime + l:
                    ok = 4
                if pos[0] > 2 * l and pos[0] <= 3 * l and pos[1] >= 3 / 4 * latime + l and pos[
                    1] <= 3 / 4 * latime + 180:
                    ok = 5
                if pos[0] > 800 and pos[1] > 3 / 4 * latime and pos[1] < 3 / 4 * latime + 1 / 8 * latime:
                    traseuu = 0
                if pos[0] > 700 and pos[1] > 3 / 4 * latime + 1 / 8 * latime:
                    lati = posi
                    posi = []
                    for i in range(len(posi)):
                        posi.append(lati[i][0], lati[i][1], (255, 255, 255))
                    traseuu = 1
                if ok == 1 and pos[1] <= 3 / 4 * latime:
                    posi.append((pos[0] - pos[0] % lat, pos[1] - pos[1] % lat, (255, 255, 0)))
                if ok == 0 and pos[1] <= 3 / 4 * latime:
                    posi.append((pos[0] - pos[0] % lat, pos[1] - pos[1] % lat, (0, 0, 255)))
                if ok == 2 and pos[1] <= 3 / 4 * latime:
                    posi.append((pos[0] - pos[0] % lat, pos[1] - pos[1] % lat, (255, 255, 255)))
                if ok == 3 and pos[1] <= 3 / 4 * latime:
                    posi.append((pos[0] - pos[0] % lat, pos[1] - pos[1] % lat, (0, 255, 0)))
                if ok == 4 and pos[1] <= 3 / 4 * latime:
                    posi.append((pos[0] - pos[0] % lat, pos[1] - pos[1] % lat, (255, 0, 0)))
                if ok == 5 and pos[1] <= 3 / 4 * latime:
                    posi.append((pos[0] - pos[0] % lat, pos[1] - pos[1] % lat, (255, 0, 255)))
        for i in range(len(posi)):
            x = posi[i][0]
            y = posi[i][1]
            patrat = pygame.Rect(x, y, lat, lat)
            pygame.draw.rect(screen, posi[i][2], patrat)
        pygame.draw.rect(screen, (255, 255, 0), galben)
        pygame.draw.rect(screen, (0, 0, 255), albastru)
        pygame.draw.rect(screen, (0, 0, 0), alb, 2)
        pygame.draw.rect(screen, (0, 255, 0), verde)
        pygame.draw.rect(screen, (255, 0, 0), rosu)
        pygame.draw.rect(screen, (255, 0, 255), mov)
        pygame.draw.rect(screen, (0, 0, 0), traseu, 2)
        pygame.draw.rect(screen, (0, 0, 0), nou, 2)
        text = fontt.render("GATA", 1, (0, 0, 0))
        screen.blit(text, (750, int(3 / 4 * latime + 1 / 16 * latime - 10)))
        text = fontt.render("RESTART", 1, (0, 0, 0))
        screen.blit(text, (730, int(3 / 4 * latime + 1 / 16 * latime + 100)))
        x = 0
        y = 0
        if traseuu == 1:
            for i in range(int(latime / lat)):
                pygame.draw.aaline(screen, (0, 0, 0), (x + (i + 1) * lat, 0), (x + (i + 1) * lat, latime * 3 / 4))
            for i in range(int(latime / 4 * 3 / lat)):
                pygame.draw.aaline(screen, (0, 0, 0), (0, y + (i + 1) * lat), (latime, y + (i + 1) * lat))

        pygame.display.update()



cloc = pygame.time.Clock()
screen = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Jocurile lui Andrei")
fontt = pygame.font.SysFont('comicsans', 20)
fonttt = pygame.font.SysFont('comicsans', 25)
uii=0
run=True
patratel = pygame.Rect(100,120, 100, 70)
patratel2 = pygame.Rect(300,120, 100, 70)
patratel3=pygame.Rect(100, 250,100,70)
patratel4 = pygame.Rect(300,250, 100, 70)
while run:
    while uii==0:
        screen.fill((80,80,80))
        pygame.draw.rect(screen, (100,100,150), patratel)
        pygame.draw.rect(screen, (100, 150, 100), patratel2)
        pygame.draw.rect(screen,(150,100,100), patratel3)
        pygame.draw.rect(screen, (60, 100, 100), patratel4)

        textt = fonttt.render("UN FEL DE", 1, (0, 0, 0))
        texttT = fonttt.render("SHOOTER", 1, (0, 0, 0))
        screen.blit(textt, (105, 140))
        screen.blit(texttT, (105, 155))

        textt = fonttt.render("UN FEL DE", 1, (0, 0, 0))
        texttT = fonttt.render("PAINT", 1, (0, 0, 0))
        screen.blit(textt, (305, 140))
        screen.blit(texttT, (325, 155))


        textt = fonttt.render("0 SI X", 1, (0, 0, 0))
        texttT = fonttt.render("PE BUNE", 1, (0, 0, 0))
        screen.blit(textt, (125, 267))
        screen.blit(texttT, (112, 282))


        textt = fonttt.render("UN FEL DE", 1, (0, 0, 0))
        texttT = fonttt.render("HANGMAN", 1, (0, 0, 0))
        screen.blit(textt, (305, 267))
        screen.blit(texttT, (305, 282))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                print (pos)
                if pos[0]>100 and pos[0]<200 and pos[1]>120 and pos[1] <190 and uii==0:
                    uii=1
                if pos[0] > 300 and pos[0] < 400 and pos[1] > 120 and pos[1] < 190 and uii == 0:
                    uii = 2
                if pos[0] > 100 and pos[0] < 200 and pos[1] > 250 and pos[1] < 320 and uii == 0:
                    uii = 3
                if pos[0] > 300 and pos[0] < 400 and pos[1] > 250 and pos[1] < 320 and uii == 0:
                    uii = 4

        if uii==1:
           shooter()
        if uii==2:
            paint()
        if uii==3:
            plm()
        if uii==4:
            spanzuratoare()
        pygame.display.update()



