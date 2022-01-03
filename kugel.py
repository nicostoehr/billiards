import pygame

class Kugel:
    def __init__(self, x, y, x_velocity, y_velocity, type, number, Bandenbreite, Breite, Kugelradius, state=1):
        self._x = x
        self._y = y
        self._x_velocity = x_velocity
        self._y_velocity = y_velocity
        self._Bandenbreite = Bandenbreite
        self._Breite = Breite
        self._Kugelradius = Kugelradius
        self._type = type
        #1=Halb, 2=Volle, 3=Schwarz, 4=Weiß
        self._number = number
        self._state = state
        #1 = Normal, 2 = Draußen
        self._font = pygame.font.SysFont("Impact", Kugelradius)

    def get_state(self):
        return self._state

    def set_state(self, State):
        self._state = State

    def get_number(self):
        return self._number

    def get_type(self):
        return self._type

    def set_x(self, XWert):
        self._x = XWert

    def set_y(self, YWert):
        self._y = YWert

    def get_x_velocity(self):
        return self._x_velocity

    def get_y_velocity(self):
        return self._y_velocity

    def get_Kugelradius(self):
        return self._Kugelradius

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x_velocity(self, NewVelocity):
        self._x_velocity = NewVelocity

    def set_y_velocity(self, NewVelocity):
        self._y_velocity = NewVelocity

    def zeichnen(self, screen):
        YELLOW = (255, 255, 0)
        GREEN = (60, 120, 0)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        VIOLET = (200, 0, 200)
        ORANGE = (255, 100, 0)
        BROWN = (150, 100, 50)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        Colors = [YELLOW, BLUE, RED, VIOLET, ORANGE, GREEN, BROWN]

        if self._number == 8:
            pygame.draw.circle(screen, BLACK, (self._x, self._y), self._Kugelradius)
            x = self._font.render(str(self._number), 0, WHITE)
            screen.blit(x, (self._x-self._Kugelradius//4, self._y-self._Kugelradius//1.5))
        elif self._number == 16:
            pygame.draw.circle(screen, WHITE, (self._x, self._y), self._Kugelradius)
        else:
            if self._number < 8:
                pygame.draw.circle(screen, Colors[self._number%8-1], (self._x, self._y), self._Kugelradius)
                x = self._font.render(str(self._number), 0, BLACK)
                screen.blit(x, (self._x - self._Kugelradius // 4, self._y - self._Kugelradius // 1.5))
            else:
                if self._number == 9:
                    pygame.draw.circle(screen, Colors[self._number % 8 - 1], (self._x, self._y), self._Kugelradius)
                    pygame.draw.circle(screen, WHITE, (self._x, self._y), int(self._Kugelradius // 1.5))
                    x = self._font.render(str(self._number), 0, BLACK)
                    screen.blit(x, (self._x - self._Kugelradius // 4, self._y - self._Kugelradius // 1.5))
                else:
                    pygame.draw.circle(screen, Colors[self._number%8-1], (self._x, self._y), self._Kugelradius)
                    pygame.draw.circle(screen, WHITE, (self._x, self._y), int(self._Kugelradius//1.5))
                    x = self._font.render(str(self._number), 0, BLACK)
                    screen.blit(x, (self._x - self._Kugelradius // 2, self._y - self._Kugelradius // 1.5))


    def reibung(self):
        if self._x_velocity>=0.01: self._x_velocity=self._x_velocity*0.993
        elif self._x_velocity<-0.01: self._x_velocity=self._x_velocity*0.993
        else:
            self._x_velocity = 0
            self._y_velocity = 0
        if self._y_velocity>=0.01: self._y_velocity=self._y_velocity*0.993
        elif self._y_velocity<-0.01: self._y_velocity=self._y_velocity*0.993
        else:
            self._y_velocity = 0
            self._x_velocity = 0

    def naechste_position(self, screen):
        self._x += self._x_velocity
        self._y += self._y_velocity

        self.reibung()
        self.zeichnen(screen)

