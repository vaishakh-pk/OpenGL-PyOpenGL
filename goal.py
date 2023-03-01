from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

windowsize=600
x=0
y=0
xb=0
rw=300
lw=240
mode=0

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-windowsize,windowsize,-windowsize,windowsize)

def draw():
    global x,y,rw,lw,xb
    glClear(GL_COLOR_BUFFER_BIT)

    #BALL
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0+xb,0+20)
    for i in range (0,361):
        glVertex2f(xb+20*math.cos(i*math.pi/180),y+20*math.sin(i*math.pi/180)+20)
    glEnd()

##PLAYER
    glColor3f(0,0,0)
    #HEAD
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-400+x,100)
    for i in range (0,361):
        glVertex2f(x+30*math.cos(i*math.pi/180)-400,y+30*math.sin(i*math.pi/180)+100)
    glEnd()

    #BODY
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-400+x,100+y)
    glVertex2f(-400+x,20+y)
    glEnd()

    #HAND
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(-400+x,60+y)
    glVertex2f(-400+x+30*math.cos(rw*math.pi/180),60+y+30*math.sin(rw*math.pi/180))
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(-400+x,60+y)
    glVertex2f(-400+x+30*math.cos(lw*math.pi/180),(60+y+30*math.sin(lw*math.pi/180)))
    glEnd()

    #LEGS
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(-400+x,20+y)
    glVertex2f(-400+x+30*math.cos(rw*math.pi/180),20+y+30*math.sin(rw*math.pi/180))
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(-400+x,20+y)
    glVertex2f(-400+x+30*math.cos(lw*math.pi/180),(20+y+30*math.sin(lw*math.pi/180)))
    glEnd()

    #POST
    glColor3f(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(500,0)
    glVertex2f(500,200)
    glVertex2f(560,180)
    glVertex2f(560,0)
    glEnd()

    #GROUND
    glColor3f(0,1,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-windowsize,0)
    glVertex2f(windowsize,0)
    glVertex2f(windowsize,-windowsize)
    glVertex2f(-windowsize,-windowsize)
    glEnd()


    glutSwapBuffers()

def animate(temp):
    global mode,x,rw,lw,xb
    if mode==0:
        x+=1
        rw-=1
        lw+=1
        if lw==300:
            mode=1
    if mode==1:
        x+=1
        rw+=1
        lw-=1
        if rw==300:
            mode=0
    if x==(380):
        mode=2

    if mode==2:
        xb+=1
        if xb==540:
            mode=3
        

    glutPostRedisplay()
    glutTimerFunc(int(400/60),animate,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowsize,windowsize)
    glutInitWindowPosition(50,50)
    glutCreateWindow("GOAL")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(draw)
    init()
    glutMainLoop()

main()