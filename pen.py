from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

windowsize=500
x=0
y=0
angle=270
fps=60
mode=1



def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def drawpend():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(x,y)
    glVertex2f(300*math.cos(angle*math.pi/180),300*math.sin(angle*math.pi/180))
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,0)
    glVertex2f(300*math.cos(angle*math.pi/180)+x,300*math.sin(angle*math.pi/180)+y)

    for i in range (0,361,1):
        glVertex2f(70*math.cos(i*math.pi/180)+300*math.cos(angle*math.pi/180)+x,70*math.sin(i*math.pi/180)+300*math.sin(angle*math.pi/180)+y)
    glEnd()

    glutSwapBuffers()

def animate(temp):
    global angle,mode
    
    print(mode,angle)

    if(mode==1):
        angle=angle+1
        if(angle==300):
            mode=0
    
    if(mode==0):
        angle=angle-1
        if(angle==240):
            mode=1


    glutPostRedisplay()
    glutTimerFunc(int(1500/fps),animate,0)

def main():
    glutInit()
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(drawpend)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawpend)
    init()
    glutMainLoop()

main()
