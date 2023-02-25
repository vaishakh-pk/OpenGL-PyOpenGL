from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

windowsize=600
er=0
count=2
mode=0
fps=60

def init():
    glClearColor(0,0,0.2,1)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def draw():
    global er,count
    #Volcano triangle
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0.5,0)
    glVertex2f(-300,-200)
    glVertex2f(300,-200)
    glVertex2f(0,200)
    glEnd()

    #moon
    
    glBegin(GL_TRIANGLE_FAN)
    glColor4f(0.5,0.5,0.5,1)
    glVertex2f(300,300)

    for i in range(0,361,1):
        glVertex2f((100)*math.cos(i*math.pi/180)+300,300+(100)*math.sin(i*math.pi/180))
    glEnd()

    #volcano opening

    glBegin(GL_TRIANGLE_FAN)
    glColor4f(0,0,0.2,1)
    glVertex2f(0,200)

    for i in range(0,361,1):
        glVertex2f((100)*math.cos(i*math.pi/180),200+(100)*math.sin(i*math.pi/180))
    glEnd()

    #Eruption
    glPointSize(6)
    glBegin(GL_POINTS)
    glColor3f(1,0,0)
    er=0
    for j in range(0,count,1):
        for i in range(233,308,1):
            glVertex2f((100+er)*math.cos(i*math.pi/180),200+(100+er)*math.sin(i*math.pi/180))
        er+=1
    glEnd()
    
    #Ground

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0.4,0)
    glVertex2f(-windowsize,-200)
    glVertex2f(windowsize,-200)
    glVertex2f(windowsize,-windowsize)
    glVertex2f(-windowsize,-windowsize)
    glEnd()


    glutSwapBuffers()

def animate(temp):
    global mode,count,fps
    if mode==0:
        count+=1
        if count==10:
            mode==1

    if mode==1:
        pass

    glutPostRedisplay()
    glutTimerFunc(int(1000/fps),animate,0)





def main():
    glutInit()
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("BOUNCING")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(draw)
    init()
    glutMainLoop()

main()