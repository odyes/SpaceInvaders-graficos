from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

#NARANJA


class Invasor_tres(Modelo):

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
            glBegin(GL_TRIANGLES)
            glColor3f(0.72, 0.53, 0.3)
            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            # for i in range(0, 360, 10):
            #     componente_x=0.07*math.cos(i*math.pi/180.0)
            #     componente_y=0.07*math.sin(i*math.pi/180.0)
            #     glVertex3f(componente_x, componente_y, 0.0)
            glEnd()

            glPopMatrix()
            self.dibujar_bounding_box() 
