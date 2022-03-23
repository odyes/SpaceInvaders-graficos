from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

##VERDEE

class Invasor_uno(Modelo):

    vivo=True
    contador_tiempo = 0.0
    tiempo_anterior = 0.0
    activos_enemigos = 1

    # posiciones_enemigos = [
    #     [-0.5, 0.75, 0.0], 
    #     [-0.1, 0.75, 0.0], 
    #     [0.3, 0.75, 0.0]
    #     ]
    # velocidades_enemigos = [0.1, 0.1, 0.1]
    # direcciones_enemigos = [0,0,0]

    def __init__(self, x, y, direccion, velocidad):
        super().__init__(x, y, 0.0, velocidad, direccion)
        self.extremo_izquierdo=0.05
        self.extremo_derecho=0.05
        self.extremo_inferior=0.05
        self.extremo_superior=0.05


    def actualizar(self, tiempo_delta):
        if self.vivo:
            #cantidad_movimiento = self.velocidad * tiempo_delta
            #self.posicion_x = self.posicion_x + (math.cos(self.direccion * math.pi / 180.0) * cantidad_movimiento)
            #self.posicion_y = self.posicion_y + (math.sin(self.direccion * math.pi / 180.0) * cantidad_movimiento)
            
            # if glfw.get_time() > 3.0:
            #     self.activos_enemigos[2] = 1
            # if glfw.get_time() > 7.0:
            #     self.activos_enemigos[1] = 1

            # self.contador_tiempo = self.contador_tiempo + tiempo_delta
            # if self.contador_tiempo >= 1.0:
            #     self.contador_tiempo = self.contador_tiempo - 1.0
            #     for i in range(3):
            #         self.velocidades_enemigos[i] = self.velocidades_enemigos[i] + 0.01
            # for i in range(3):
            #     if self.activos_enemigos[i]:
            #         cantidad_movimiento = self.velocidades_enemigos[i] * tiempo_delta
            #         if self.direcciones_enemigos[i] == 0:
            #             self.posiciones_enemigos[i][0] = self.posiciones_enemigos[i][0] - cantidad_movimiento
            #             if self.posiciones_enemigos[i][0] <= -0.75:
            #                 self.direcciones_enemigos[i] = 1
            #         else:
            #             self.posiciones_enemigos[i][0] = self.posiciones_enemigos[i][0] + (cantidad_movimiento*5)
            #             self.posiciones_enemigos[i][1] = self.posiciones_enemigos[i][1] - (cantidad_movimiento/2)
            #             if self.posiciones_enemigos[i][0] >= 0.75:
            #                 self.direcciones_enemigos[i] = 0
            cantidad_movimiento = self.velocidad * tiempo_delta
            self.posicion_x = self.posicion_x + (math.cos(self.direccion * math.pi / 180.0) * cantidad_movimiento)
            self.posicion_y = self.posicion_y + (math.sin(self.direccion * math.pi / 180.0) * cantidad_movimiento)

            if self.posicion_x > 1.05:
                self.posicion_x = -1.0
            if self.posicion_x < -1.05:
                self.posicion_x = 1.0

            if self.posicion_y > 1.05:
                self.posicion_y = -0.6
            if self.posicion_y < -1.0:
                self.posicion_y = 1.05



    def dibujar(self):
        if self.vivo:

            glPushMatrix()

            glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.3, 0.72, 0.37)
            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            # for i in range(0, 360, 10):
            #     componente_x=0.07*math.cos(i*math.pi/180.0)
            #     componente_y=0.07*math.sin(i*math.pi/180.0)
            #     glVertex3f(componente_x, componente_y, 0.0)
            glEnd()
            glPopMatrix()

            self.dibujar_bounding_box() 