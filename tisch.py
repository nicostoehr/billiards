import pygame
import math
from kugel import Kugel

def MakierungenX(x, y, screen, Breite, Bandenbreite):
    for i in range(1, 4):
        pygame.draw.polygon(screen, (150,150,150),
                            [(x + Breite // 4 * i, y + Bandenbreite // 2),
                             (x + Breite // 4 * i + Bandenbreite // 2, y),
                             (x + Breite // 4 * i + Bandenbreite, y + Bandenbreite // 2),
                             (x + Breite // 4 * i + Bandenbreite // 2, y + Bandenbreite)])

def MakierungenY(x,y, screen, Breite, Bandenbreite):
    for i in range(1,4):
        pygame.draw.polygon(screen, (150,150,150),
                            [(x, y + Breite//4 * i),
                             (x+Bandenbreite//2, y + Breite//4 * i- Bandenbreite//2),
                             (x+Bandenbreite, y + Breite//4 * i),
                             (x+Bandenbreite//2, y + Breite//4 * i + Bandenbreite//2)])

def abprallen(Kugel, Breite, Bandenbreite, Lochlaenge, Lochkathete):
    xpos = Kugel.get_x()
    ypos = Kugel.get_y()
    Kugelradius = Kugel.get_Kugelradius()
    if xpos > Bandenbreite+Lochkathete and xpos < Breite-Lochlaenge//2+1 or xpos > Breite+Lochlaenge//2-1 and xpos < Breite*2-Bandenbreite-Lochkathete+5:
        if ypos <= Bandenbreite+Kugelradius or ypos >= Breite-Bandenbreite-Kugelradius:
            Kugel.set_y_velocity(Kugel.get_y_velocity()*(-0.99))
            Kugel.set_x(Kugel.get_x() + Kugel.get_x_velocity())
            Kugel.set_y(Kugel.get_y() + Kugel.get_y_velocity())
    if ypos > Bandenbreite+Lochkathete and ypos < Breite-Bandenbreite-Lochkathete:
        if xpos <= Bandenbreite+Kugelradius or xpos >= Breite*2-Bandenbreite-Kugelradius:
            Kugel.set_x_velocity(Kugel.get_x_velocity()*(-0.99))
            Kugel.set_x(Kugel.get_x()+Kugel.get_x_velocity())
            Kugel.set_y(Kugel.get_y()+Kugel.get_y_velocity())

def tisch(screen, Bandenbreite, Breite, Lochlaenge, Lochkatheten):
    BLACK = (0, 0, 0)
    GRAY = (150, 150, 150)
    DARKGREEN = (30, 120, 30)
    GREEN = (100, 200, 100)
    pygame.draw.rect(screen, DARKGREEN, (0,0,Breite*2,Breite))
    pygame.draw.rect(screen, GREEN, (Bandenbreite,Bandenbreite,Breite*2-Bandenbreite*2,Breite-Bandenbreite*2))
    pygame.draw.rect(screen, BLACK, (Breite-Lochlaenge//2, 0, Lochlaenge, Bandenbreite))
    pygame.draw.rect(screen, BLACK, (Breite-Lochlaenge//2, Breite-Bandenbreite, Lochlaenge, Bandenbreite))
    MakierungenX(0,0, screen, Breite, Bandenbreite)
    MakierungenX(Breite,0, screen, Breite, Bandenbreite)
    MakierungenX(0,Breite-Bandenbreite, screen, Breite, Bandenbreite)
    MakierungenX(Breite,Breite-Bandenbreite, screen, Breite, Bandenbreite)
    MakierungenY(0,0, screen, Breite, Bandenbreite)
    MakierungenY(Breite*2-Bandenbreite, 0, screen, Breite, Bandenbreite)

    pygame.draw.polygon(screen, BLACK,[(Bandenbreite+Lochkatheten,Bandenbreite),
                                       (Bandenbreite,Bandenbreite+Lochkatheten),
                                       (Bandenbreite-100, Bandenbreite + Lochkatheten-100),
                                       (Bandenbreite + Lochkatheten-100, Bandenbreite-100)])

    pygame.draw.polygon(screen, BLACK,[(Breite*2-Bandenbreite-Lochkatheten,Bandenbreite),
                                       (Breite*2-Bandenbreite,Bandenbreite+Lochkatheten),
                                       (Breite * 2 - Bandenbreite+100, Bandenbreite + Lochkatheten-100),
                                       (Breite * 2 - Bandenbreite - Lochkatheten+100, Bandenbreite-100)])

    pygame.draw.polygon(screen, BLACK,[(Bandenbreite, Breite-Bandenbreite-Lochkatheten),
                                       (Bandenbreite+Lochkatheten, Breite-Bandenbreite),
                                       (Bandenbreite + Lochkatheten - 100, Breite - Bandenbreite + 100),
                                       (Bandenbreite -100 , Breite - Bandenbreite - Lochkatheten + 100)])

    pygame.draw.polygon(screen, BLACK,[(Breite*2-Bandenbreite-Lochkatheten, Breite-Bandenbreite),
                                       (Breite*2-Bandenbreite, Breite-Bandenbreite-Lochkatheten),
                                       (Breite * 2 - Bandenbreite+100, Breite - Bandenbreite - Lochkatheten+100),
                                       (Breite * 2 - Bandenbreite - Lochkatheten+100, Breite - Bandenbreite+100)])

    pygame.draw.rect(screen, GRAY, (0,Breite,Breite*2, Breite))

def treffer(Kugel, screen, Kugelradius, Breite, Bandenbreite, Lochkatheten, Lochlaenge):
    rec1 = pygame.draw.polygon(screen, (0,0,0), [(Bandenbreite + Lochkatheten, Bandenbreite),
                                               (Bandenbreite, Bandenbreite + Lochkatheten),
                                               (Bandenbreite - 100, Bandenbreite + Lochkatheten - 100),
                                               (Bandenbreite + Lochkatheten - 100, Bandenbreite - 100)])
    rec2 = pygame.draw.polygon(screen, (0,0,0), [(Breite * 2 - Bandenbreite - Lochkatheten, Bandenbreite),
                                               (Breite * 2 - Bandenbreite, Bandenbreite + Lochkatheten),
                                               (Breite * 2 - Bandenbreite + 100, Bandenbreite + Lochkatheten - 100),
                                               (Breite * 2 - Bandenbreite - Lochkatheten + 100, Bandenbreite - 100)])
    rec3 = pygame.draw.polygon(screen, (0,0,0), [(Bandenbreite, Breite - Bandenbreite - Lochkatheten),
                                               (Bandenbreite + Lochkatheten, Breite - Bandenbreite),
                                               (Bandenbreite + Lochkatheten - 100, Breite - Bandenbreite + 100),
                                               (Bandenbreite - 100, Breite - Bandenbreite - Lochkatheten + 100)])
    rec4 = pygame.draw.polygon(screen, (0,0,0), [(Breite * 2 - Bandenbreite - Lochkatheten, Breite - Bandenbreite),
                                               (Breite * 2 - Bandenbreite, Breite - Bandenbreite - Lochkatheten),
                                               (Breite * 2 - Bandenbreite + 100, Breite - Bandenbreite - Lochkatheten + 100),
                                               (Breite * 2 - Bandenbreite - Lochkatheten + 100, Breite - Bandenbreite + 100)])
    rec5 = pygame.draw.rect(screen, (0,0,0), (Breite - Lochlaenge // 2, 0, Lochlaenge, Bandenbreite))
    rec6 = pygame.draw.rect(screen, (0,0,0), (Breite - Lochlaenge // 2, Breite - Bandenbreite, Lochlaenge, Bandenbreite))
    temp = pygame.draw.rect(screen, (255,255,255),(Kugel.get_x()-Kugelradius//2,Kugel.get_y()-Kugelradius//2,Kugelradius*1.5,Kugelradius*1.5))

    obenlinks = pygame.Rect.colliderect(rec1, temp)
    obenrechts = pygame.Rect.colliderect(rec2, temp)
    untenlinks = pygame.Rect.colliderect(rec3, temp)
    untenrechts = pygame.Rect.colliderect(rec4, temp)
    obenmitte = pygame.Rect.colliderect(rec5, temp)
    untenmitte = pygame.Rect.colliderect(rec6, temp)
    if obenlinks or obenrechts or untenlinks or untenrechts or obenmitte or untenmitte:
        return [True, Kugel.get_type()]
    else: return [False, Kugel.get_type()]

def kollision(Kugel_a, Kugel_b, Kugelradius):
    xdif=Kugel_a.get_x()+Kugel_a.get_x_velocity()-Kugel_b.get_x()+Kugel_b.get_x_velocity()
    ydif=Kugel_a.get_y()+Kugel_a.get_y_velocity()-Kugel_b.get_y()+Kugel_b.get_y_velocity()

    if math.sqrt(xdif*xdif+ydif*ydif)<Kugelradius*2:
        #print("!")
        return [xdif, ydif, True]
    else: return [None, None, False]

def queu(screen, MousePos, x, y, Kugelradius):
    xdif=abs(MousePos[0]-x)
    ydif=abs(MousePos[1]-y)
    xr=1/(xdif+ydif)*xdif
    yr=1/(xdif+ydif)*ydif

    if MousePos[0]>x:
        addx = Kugelradius*2
    else:
        addx = Kugelradius*(-2)
    if MousePos[1]>y:
        addy = Kugelradius*2
    else:
        addy = Kugelradius*(-2)
    pygame.draw.line(screen, (150, 75, 0), (x+addx*xr, y+addy*yr),(x+addx*8*xr, y+addy*8*yr),5)



