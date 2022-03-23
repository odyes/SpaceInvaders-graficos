from OpenGL.GL import *
from invasor_uno import Invasor_uno
from invasor_dos import Invasor_dos
from invasor_tres import Invasor_tres
from invasor_cuatro import Invasor_cuatro
from invasor_cinco import Invasor_cinco
from glew_wish import *
import glfw
import math 
from Nave import *
from Fondo import *

import random

window = None

tiempo_anterior = 0.0

estado_anterior_espacio = glfw.RELEASE

nave = Nave()
invasores = []
fondo = Fondo()

def actualizar():
    global tiempo_anterior
    global window

    tiempo_actual = glfw.get_time()
    # Cuanto tiempo paso entre la ejecucion actual
    # y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    nave.actualizar(window, tiempo_delta)
    for invasor in invasores:
        if invasor.vivo:
            invasor.actualizar(tiempo_delta)
            if invasor.colisionando(nave):
                nave.herido=True
                glfw.set_window_should_close(window,True)
            for bala in nave.balas:
                if bala.disparando:
                    if invasor.colisionando(bala):
                        bala.disparando=False
                        invasor.vivo=False
    
    invasor.actualizar(tiempo_delta)
    tiempo_anterior = tiempo_actual
    
def colisionando(x1,y1,wl1,wr1,hu1,hd1,x2,y2,wl2,wr2,hu2,hd2):

    colisionando = False
    
    #Método de bounding box:
    #Extrema derecha del primero >= Extrema izquierda segundo
    #Extrema izquierda del primero <= Extrema derecha segundo
    #Extremo superior del primero >= Extremo inferior del segundo
    #Extremo inferior del primero <= Extremo superior del segundo
    if (x1 + wr1 >= x2 - wl2 
        and x1 - wl1 <= x2 + wr2 
        and y1 + hu1 >= y2 - hd2 
        and y1 - hd1 <= y2 + hu2):
        
        colisionando = True 

    return colisionando
 
def draw():

    fondo.dibujar()
    nave.dibujar()
    for invasor in invasores:
        invasor.dibujar()

def inicializar_invasor_uno():
    for i in range(3):
        posicion_x = -0.7
        posicion_y = 0.6
        direccion = random.random() * 360
        velocidad = 0.3
        invasores.append(Invasor_uno(posicion_x, posicion_y, direccion, velocidad))

def inicializar_invasor_dos():
    for i in range(3):
        posicion_x = 0.8
        posicion_y = 0.2
        direccion = random.random() * 360
        velocidad = 0.3
        invasores.append(Invasor_dos(posicion_x, posicion_y, direccion, velocidad))
        
def inicializar_invasor_tres():
    for i in range(3):
        posicion_x = -0.5
        posicion_y = 0.7
        direccion = random.random() * 360
        velocidad = 0.3
        invasores.append(Invasor_tres(posicion_x, posicion_y, direccion, velocidad))
        
def inicializar_invasor_cuatro():
    for i in range(3):
        posicion_x = -0.3
        posicion_y = 0.2
        direccion = random.random() * 360
        velocidad = 0.3
        invasores.append(Invasor_cuatro(posicion_x, posicion_y, direccion, velocidad))


def inicializar_invasor_cinco():
    for i in range(3):
        posicion_x = 0.6
        posicion_y = 0.4
        direccion = random.random() * 360
        velocidad = 0.3
        invasores.append(Invasor_cinco(posicion_x, posicion_y, direccion, velocidad))


def main():
    global window

    width = 700
    height = 700
    # Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi Juego Piratongo", None, None)

    # Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    # Establecer el contexto
    glfw.make_context_current(window)

    # Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    # Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    # Imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    inicializar_invasor_uno()
    inicializar_invasor_dos()
    inicializar_invasor_tres()
    inicializar_invasor_cuatro()
    inicializar_invasor_cinco()

    # Draw loop
    while not glfw.window_should_close(window):
        # Establecer el viewport
        # glViewport(0,0,width,height)
        # Establecer color de borrado
        glClearColor(0.03,0.03,0.08,1 )
        # Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        actualizar()
        # Dibujar
        draw()

        # Polling de inputs
        glfw.poll_events()

        # Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()