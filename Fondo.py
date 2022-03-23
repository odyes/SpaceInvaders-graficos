from OpenGL.GL import *
from glew_wish import *
from Modelo import *
import glfw
import math

class Fondo(Modelo):
    
    def __init__(self):
        super().__init__(0.0, 0.0, 0.0, 0.0, 0.0)

    def dibujar(self):
        glBegin(GL_LINES)
        glColor3f(1.0,1.0,1.0)
        #####
        glVertex3f(-0.4,0.85,0)
        glVertex3f(-0.4,0.84,0)

        glVertex3f(0.3,0.45,0)
        glVertex3f(0.3,0.46,0)

        glVertex3f(0.2,0.97,0)
        glVertex3f(0.2,0.98,0)

        glVertex3f(0.4,0.17,0)
        glVertex3f(0.4,0.18,0)

        glVertex3f(0.4,-0.47,0)
        glVertex3f(0.4,-0.48,0)

        glVertex3f(0.3,-0.45,0)
        glVertex3f(0.3,-0.46,0)

        glVertex3f(-0.1,-0.55,0)
        glVertex3f(-0.1,-0.54,0)

        glVertex3f(-0.7,-0.15,0)
        glVertex3f(-0.7,-0.14,0)

        glVertex3f(-0.56,-0.98,0)
        glVertex3f(-0.56,-0.96,0)

        glVertex3f(-0.52,-0.62,0)
        glVertex3f(-0.52,-0.6,0)

        glVertex3f(-0.87,-0.93,0)
        glVertex3f(-0.87,-0.95,0)

        glVertex3f(0.82,-0.33,0)
        glVertex3f(0.82,-0.34,0)

        glVertex3f(0.1,-0.23,0)
        glVertex3f(0.1,-0.24,0)
        
        glVertex3f(0.2,-0.53,0)
        glVertex3f(0.2,-0.54,0)

        glVertex3f(0.8,-0.32,0)
        glVertex3f(0.82,-0.34,0)

        glVertex3f(0.86,-0.12,0)
        glVertex3f(0.86,-0.13,0)

        glVertex3f(-0.31,-0.22,0)
        glVertex3f(-0.31,-0.23,0)

        glVertex3f(0.23,-0.26,0)
        glVertex3f(0.23,-0.26,0)

        glVertex3f(0.0,-0.53,0)
        glVertex3f(0.0,-0.54,0)

        glVertex3f(0.1,0.53,0)
        glVertex3f(0.1,0.54,0)

        glVertex3f(-0.23,-0.15,0)
        glVertex3f(-0.23,-0.16,0)

        glVertex3f(-0.42,-0.15,0)
        glVertex3f(-0.42,-0.16,0)
        
        glVertex3f(-0.93,0.43,0)
        glVertex3f(-0.93,0.44,0)

        glVertex3f(-0.46,0.42,0)
        glVertex3f(-0.46,0.43,0)

        glVertex3f(0.23,0.86,0)
        glVertex3f(0.23,0.87,0)

        glVertex3f(0.32,-0.9,0)
        glVertex3f(0.32,-0.91,0)

        glVertex3f(0.23,-0.15,0)
        glVertex3f(0.23,-0.16,0)

        ##Asterisco
        glVertex3f(0.4,0.3,0)
        glVertex3f(0.4,0.33,0)

        ##glVertex3f(0.38,0.3,0)
        ##glVertex3f(0.41,0.33,0)

        ##glVertex3f(0.4,0.3,0)
        ##glVertex3f(0.38,0.28,0)
        
        ##
        glVertex3f(-0.7,0.4,0)
        glVertex3f(-0.7,0.3,0)

        glVertex3f(-0.8,0.35,0)
        glVertex3f(-0.6,0.35,0)

        glVertex3f(-0.75,0.33,0)
        glVertex3f(-0.65,0.37,0)

        glVertex3f(-0.75,0.37,0)
        glVertex3f(-0.65,0.33,0)

        glVertex3f(-0.2,0.05,0)
        glVertex3f(-0.2,0.06,0)

        glVertex3f(-0.26,0.15,0)
        glVertex3f(-0.26,0.15,0)

        glVertex3f(0.3,0.37,0)
        glVertex3f(0.3,0.36,0)

        glVertex3f(-0.35,0.1,0)
        glVertex3f(-0.35,0.1,0)

        ##glVertex3f(0.5,0.23,0)
        ##glVertex3f(0.5,0.24,0)

        ##
        glVertex3f(0.7,-0.4,0)
        glVertex3f(0.7,-0.3,0)

        glVertex3f(0.8,-0.35,0)
        glVertex3f(0.6,-0.35,0)

        glVertex3f(0.75,-0.33,0)
        glVertex3f(0.65,-0.37,0)

        glVertex3f(0.75,-0.37,0)
        glVertex3f(0.65,-0.33,0)

        ##
        glVertex3f(0.9,-0.7,0)
        glVertex3f(0.9,-0.6,0)

        glVertex3f(1.0,-0.65,0)
        glVertex3f(0.8,-0.65,0)

        glVertex3f(0.95,-0.63,0)
        glVertex3f(0.85,-0.67,0)

        glVertex3f(0.95,-0.67,0)
        glVertex3f(0.85,-0.63,0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(.25,0.32,0.65)

        for angulo in range(0,359,5):                     ##X   ##Tamaño                        ##Altura
            glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.4,0.005*math.sin(angulo*math.pi/180)-0.3, 0)
        #for angulo in range(0,359,5):                     
        #   glVertex3f(0.005*math.cos(angulo*math.pi/180) -0.4,0.005*math.sin(angulo*math.pi/180)-0.3, 0)
        #for angulo in range(0,359,5):                     
        #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.7,0.005*math.sin(angulo*math.pi/180)+0.3, 0)
        #for angulo in range(0,359,5):                     
        #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.6,0.005*math.sin(angulo*math.pi/180)-0.9, 0)
        #for angulo in range(0,359,5):                     
        #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.7,0.005*math.sin(angulo*math.pi/180)-0.6, 0)
        #for angulo in range(0,359,5):                     
        #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.4,0.005*math.sin(angulo*math.pi/180)+0.3, 0)
        #for angulo in range(0,359,5):                     
        #   glVertex3f(0.005*math.cos(angulo*math.pi/180) -0.52,0.005*math.sin(angulo*math.pi/180)-0.38, 0)

        glEnd()

        glBegin(GL_LINES)
        glColor3f(0.95,1.0,0.0)

        glVertex3f(-0.6,0.7,0)
        glVertex3f(-0.6,0.71,0)

        glVertex3f(-0.7,0.55,0)
        glVertex3f(-0.7,0.54,0)

        glVertex3f(0.8,0.65,0)
        glVertex3f(0.8,0.64,0)

        glVertex3f(-0.1,0.75,0)
        glVertex3f(-0.1,0.74,0)
        
        glEnd()
