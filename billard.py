#####
#Dieses Spiel wurde entwickelt und getestet auf der Pygame Version 2.0.0.dev6
#Keine Garantie für Funktionalität auf anderen Versionen!
#
#Spielerwechsel funktioniert zwar, jedoch wurde nach langem probieren festgestellt, dass das Verweilen beim derzeitigen
#Spieler, wenn dieser eine Kugel von seiner Sorte eingelocht hat, nicht....
#####

import array
import pygame
import time
import math
import random
from player import Player
from tisch import tisch
from tisch import abprallen
from kugel import Kugel
from tisch import treffer
from tisch import kollision
from tisch import queu

pygame.init()

Bandenbreite = 10
Breite = 300
Lochlaenge = Breite // 12
Lochkatheten = int(math.sqrt(Lochlaenge * Lochlaenge / 2))
Kugelradius = Lochlaenge//3
font = pygame.font.SysFont("Impact", Breite//14)
fontgross = pygame.font.SysFont("Impact", Breite//6)

screen = pygame.display.set_mode((Breite*2,Breite*2))
pygame.display.set_caption("Billard")

Koordinaten=[   [Breite/2, Breite/2+Kugelradius*2.2],
                [Breite/2, Breite/2-Kugelradius*2.2],
                [Breite/2+Kugelradius*4, Breite/2],
                [Breite/2+Kugelradius*2, Breite/2-Kugelradius*1.2],
                [Breite/2+Kugelradius*2, Breite/2+Kugelradius*1.2],
                [Breite/2-Kugelradius*2, Breite/2-Kugelradius*3.4],
                [Breite/2-Kugelradius*2, Breite/2+Kugelradius*3.4],
                [Breite/2-Kugelradius*2, Breite/2-Kugelradius*1.2],
                [Breite/2-Kugelradius*2, Breite/2+Kugelradius*1.2],
                [Breite/2-Kugelradius*4, Breite/2-Kugelradius*4.4],
                [Breite/2-Kugelradius*4, Breite/2-Kugelradius*2.2],
                [Breite/2-Kugelradius*4, Breite/2],
                [Breite/2-Kugelradius*4, Breite/2+Kugelradius*2.2],
                [Breite/2-Kugelradius*4, Breite/2+Kugelradius*4.4]  ]

Kugeln=[]

for i in range(1,17):
    if i == 8:
        Kugeln.append(Kugel(Breite // 2, Breite // 2, 0, 0, 3, i, Bandenbreite, Breite, Kugelradius))
    elif i == 16:
        Kugeln.append(Kugel(Breite // 2 + Breite, Breite // 2, 0, 0, 4, i, Bandenbreite, Breite, Kugelradius))
    else:
        if i < 8:
            if len(Koordinaten) > 0:
                t = random.randint(0, len(Koordinaten) - 1)
                x = Koordinaten.pop(t)
                Kugeln.append(Kugel(x[0], x[1], 0, 0, 1, i, Bandenbreite, Breite, Kugelradius))
        if i > 8:
            if len(Koordinaten) > 0:
                t = random.randint(0, len(Koordinaten) - 1)
                x = Koordinaten.pop(t)
                Kugeln.append(Kugel(x[0], x[1], 0, 0, 2, i, Bandenbreite, Breite, Kugelradius))

clock = pygame.time.Clock()
power=0
mousepressed=False
Kugelstapelx = Bandenbreite
Kugelstapely = Breite+Bandenbreite*2+Breite//8+Kugelradius
Kugelstapelxre = Breite*2-Bandenbreite
KugelnVelocities = []
KugelnVelocity = False
spawnwhite = False

firstball = True
Halbespieler = 0

finish=False

player1 = Player(1, turn=True)
player2 = Player(2)
inrunde = False
current_turn = 0
treffer_halbe = False
treffer_ganze = False

while True:

    KugelnVelocities.clear()
    for o in Kugeln:
        if o.get_x_velocity() != 0 or o.get_y_velocity() != 0:
            KugelnVelocities.append(True)
        else:
            KugelnVelocities.append(False)

    if True in KugelnVelocities:
        KugelnVelocity = True
    else:
        KugelnVelocity = False

  #------------------------
    #print(KugelnVelocity)

    if (Kugeln[15].get_x_velocity() != 0) or (Kugeln[15].get_y_velocity() != 0) :
        inrunde = True
    if KugelnVelocity == False and inrunde:

       #Fehlerhafte abfrage aufgrund von reset problemem der treffer variablen
       #if Halbespieler == 1 and player1.get_turn() and treffer_halbe:continue
       #if Halbespieler == 2 and player2.get_turn() and treffer_halbe:continue
       #if Halbespieler == 1 and player1.get_turn() and treffer_ganze:continue
       #if Halbespieler == 2 and player2.get_turn() and treffer_ganze:continue

            current_turn += 1
            if player1.get_turn():
                player1.set_turn(False)
                player2.set_turn(True)
            elif player2.get_turn():
                player2.set_turn(False)
                player1.set_turn(True)
            inrunde = False
        #treffer_halbe = False
        #treffer_ganze = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not KugelnVelocity:
                mousepressed=True
        if event.type == pygame.MOUSEBUTTONUP:
            mousepressed= False
            MousePos = pygame.mouse.get_pos()
            xpos = Kugeln[15].get_x()
            ypos = Kugeln[15].get_y()
            xdif = abs(MousePos[0]-xpos)
            ydif = abs(MousePos[1]-ypos)
            multiplicator = power/(xdif+ydif)
            Kugel.set_x_velocity(Kugeln[15], (MousePos[0]-xpos)*multiplicator*(-1))
            Kugel.set_y_velocity(Kugeln[15], (MousePos[1]-ypos)*multiplicator*(-1))
            power=0

    if mousepressed:
        power=(power+0.05)%10


    #Treffer

    for k in Kugeln:
        t = treffer(k, screen, Kugelradius, Breite, Bandenbreite, Lochkatheten, Lochlaenge)
        if t[0]:
            if k.get_type() == 3:
                if player1.get_turn() and player1.get_achtfreigabe():
                    finish=1
                else:
                    finish=2
                if player2.get_turn() and player2.get_achtfreigabe():
                    finish=2
                else:
                    finish=1

            elif k.get_type() == 4:
                k.set_x_velocity(0)
                k.set_y_velocity(0)
                k.set_x(Kugelradius*(-2))
                k.set_y(Kugelradius*(-2))
                spawnwhite=True


            elif k.get_type() == 2:
                #Volle
                treffer_ganze = True
                k.set_state(2)
                k.set_x_velocity(0)
                k.set_y_velocity(0)
                k.set_y(Kugelstapely)
                if firstball == True:
                    if player1.get_turn():
                        Halbespieler = 2
                        firstball = False
                    else:
                        Halbespieler = 1
                        firstball = False

                if Halbespieler==1:
                    k.set_x(Kugelstapelxre)
                    Kugelstapelxre -= Kugelradius * 2 + Bandenbreite
                else:
                    k.set_x(Kugelstapelx)
                    Kugelstapelx += Kugelradius*2+Bandenbreite

            elif k.get_type() == 1:
                #Halbe
                treffer_halbe = True
                k.set_state(2)
                k.set_x_velocity(0)
                k.set_y_velocity(0)
                k.set_y(Kugelstapely)
                if firstball == True:
                    if player1.get_turn():
                        Halbespieler = 1
                        firstball = False
                    else:
                        Halbespieler = 2
                        firstball = False

                if Halbespieler==1:
                    k.set_x(Kugelstapelx)
                    Kugelstapelx += Kugelradius * 2 + Bandenbreite
                else:
                    k.set_x(Kugelstapelxre)
                    Kugelstapelxre -= Kugelradius * 2 + Bandenbreite



    if KugelnVelocity == False and spawnwhite:
        Mov = 0
        disruptdefault = False
        for z in Kugeln:
            if z.get_x()>Breite*1.5-Kugelradius*2 and z.get_x()<Breite*1.5+Kugelradius*2 and z.get_y()<Breite/2-Kugelradius*2+Mov and z.get_y()>Breite/2+Kugelradius*2+Mov:
                disruptdefault=True
        if disruptdefault==True:
            Mov+=Kugelradius*2
            disrupt2 = False
            for u in Kugeln:
                if u.get_x() > Breite * 1.5 - Kugelradius * 2 and u.get_x() < Breite * 1.5 + Kugelradius * 2 and u.get_y() < Breite / 2 - Kugelradius * 2 + Mov and u.get_y() > Breite / 2 + Kugelradius * 2 + Mov:
                    disrupt2=True
            if disrupt2==True:
                Mov+=Kugelradius*2
                disrupt3= False
                for v in Kugeln:
                    if v.get_x() > Breite * 1.5 - Kugelradius * 2 and v.get_x() < Breite * 1.5 + Kugelradius * 2 and v.get_y() < Breite / 2 - Kugelradius * 2 + Mov and v.get_y() > Breite / 2 + Kugelradius * 2 + Mov:
                        disrupt3=True
                if disrupt3==True: Mov+= Kugelradius*2
       ########################################################################
        Kugeln[15].set_x(Breite // 2 + Breite)
        Kugeln[15].set_y(Breite // 2 + Mov)
        spawnwhite = False

    tisch(screen, Bandenbreite, Breite, Lochlaenge, Lochkatheten)
    pygame.draw.rect(screen, (100,100,100), (Bandenbreite, Breite+Bandenbreite, Breite*2-Bandenbreite*2,Breite//8))
    pygame.draw.rect(screen, (255, 0, 0), (Bandenbreite*2, Breite+Bandenbreite*2, (Breite*2-Bandenbreite*4)/10*power,Breite//8-Bandenbreite*2))
    Text1 = font.render(str("Spieler 1"), 0, (255, 255, 255))
    screen.blit(Text1, (Bandenbreite, Breite*1.3))
    if Halbespieler == 1:
        Text1zusatz = font.render(str("(Ganze Kugeln)"), 0, (255, 255, 255))
        screen.blit(Text1zusatz, (Bandenbreite, Breite * 1.4))
    elif Halbespieler == 2:
        Text1zusatz = font.render(str("(Halbe Kugeln)"), 0, (255, 255, 255))
        screen.blit(Text1zusatz, (Bandenbreite, Breite * 1.4))
    Text2 = font.render(str("Spieler 2"), 0, (255, 255, 255))
    screen.blit(Text2, (Breite*2-Kugelradius*10, Breite*1.3))
    if Halbespieler == 1:
        Text2zusatz = font.render(str("(Halbe Kugeln)"), 0, (255, 255, 255))
        screen.blit(Text2zusatz, (Breite * 2 - Kugelradius * 16, Breite * 1.4))
    elif Halbespieler == 2:
        Text2zusatz = font.render(str("(Ganze Kugeln)"), 0, (255, 255, 255))
        screen.blit(Text2zusatz, (Breite * 2 - Kugelradius * 16, Breite * 1.4))

    if player1.get_turn():
        Spieleranzeige = font.render(str("Spieler 1 ist dran"), 0, (255,255,255))
        screen.blit(Spieleranzeige, (Breite-Breite//4, Breite+Bandenbreite*2))
    elif player2.get_turn():
        Spieleranzeige = font.render(str("Spieler 2 ist dran"), 0, (255,255,255))
        screen.blit(Spieleranzeige, (Breite-Breite//4, Breite+Bandenbreite*2))

    if mousepressed:
        queu(screen, pygame.mouse.get_pos(), Kugeln[15].get_x(), Kugeln[15].get_y(), Kugelradius)
    for j in Kugeln:
        for l in Kugeln:
            if j==l: continue
            else:
                if l.get_number()>j.get_number():
                    radiuskoordinaten = kollision(j, l, Kugelradius)
                    if radiuskoordinaten[2]:

                        normvector = radiuskoordinaten[0]**2 + radiuskoordinaten[1]**2
                        j_velocity = (j.get_x_velocity(), j.get_y_velocity())
                        l_velocity = (l.get_x_velocity(), l.get_y_velocity())
                        vjd = j_velocity[0] * radiuskoordinaten[0] +j_velocity[1] * radiuskoordinaten[1]
                        vld = l_velocity[0] * radiuskoordinaten[0] +l_velocity[1] * radiuskoordinaten[1]

                        if normvector != 0:
                            j.set_x(j.get_x() - j.get_x_velocity())
                            j.set_y(j.get_y() - j.get_y_velocity())
                            l.set_x(l.get_x() - l.get_x_velocity())
                            l.set_y(l.get_y() - l.get_y_velocity())

                            j.set_x_velocity((j_velocity[0] - radiuskoordinaten[0]*(vjd-vld)/normvector))
                            j.set_y_velocity((j_velocity[1] - radiuskoordinaten[1]*(vjd-vld)/normvector))
                            l.set_x_velocity((l_velocity[0] - radiuskoordinaten[0]*(vld-vjd)/normvector))
                            l.set_y_velocity((l_velocity[1] - radiuskoordinaten[1]*(vld-vjd)/normvector))


        abprallen(j, Breite, Bandenbreite, Lochlaenge, Lochkatheten)
        j.naechste_position(screen)
    clock.tick(400)

    if finish == 1:
        t = fontgross.render(str("Spieler 1 hat gewonnen"), 0, (255, 255, 255))
        screen.blit(t, (Breite / 4, Breite / 2))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()

    if finish == 2:
        t = fontgross.render(str("Spieler 2 hat gewonnen"), 0, (255, 255, 255))
        screen.blit(t, (Breite / 4, Breite / 2))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()


    pygame.display.update()

    #Check win
    if Kugeln[0].get_state() == 2 and Kugeln[1].get_state() == 2 and Kugeln[2].get_state() == 2 and Kugeln[3].get_state() == 2 and Kugeln[4].get_state() == 2 and Kugeln[5].get_state() == 2 and Kugeln[6].get_state() == 2:
        if Halbespieler == 1:
            player1.set_achtfreigabe(True)
        else:
            player2.set_achtfreigabe(True)

    if Kugeln[8].get_state() == 2 and Kugeln[9].get_state() == 2 and Kugeln[10].get_state() == 2 and Kugeln[11].get_state() == 2 and Kugeln[12].get_state() == 2 and Kugeln[13].get_state() == 2 and Kugeln[14].get_state() == 2:
         if Halbespieler == 1:
             player2.set_achtfreigabe(True)
         else:
             player1.set_achtfreigabe(True)




