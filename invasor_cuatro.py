from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

#ROJO

from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

#AMARILLOOO
class Invasor_cuatro(Modelo):

    vivo=True
    contador_tiempo = 0.0
    tiempo_anterior = 0.0
    activos_enemigos = 1


    def __init__(self, x, y, direccion, velocidad):
        super().__init__(x, y, 0.0, velocidad, direccion)
        self.extremo_izquierdo=0.05
        self.extremo_derecho=0.05
        self.extremo_inferior=0.05
        self.extremo_superior=0.05


    def actualizar(self, tiempo_delta):
        if self.vivo:
            
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
            glBegin(GL_POLYGON)
            glColor3f(0.72, 0.30, 0.30)
            # for angulo in range(0,359,5):                     ##X   ##Tamaño                        ##Altura
            #     glVertex3f(0.055*math.cos(angulo*math.pi/180),0.055*math.sin(angulo*math.pi/180), 0)
            glEnd()
            glPopMatrix()

            self.dibujar_bounding_box() 