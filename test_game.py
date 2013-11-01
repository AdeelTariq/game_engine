from baseGame import game
from settings import *
from spatials import dynSpatial
from inputHandlers import keyDownHandler
from pygame.locals import *
from controls import *
from gameState import gameState
import pygame


def moveBy_s():
    mySpatial.rect=mySpatial.rect.move(10,10)
def changeState():
    mygame.changeState('1')
def changeState2():
    mygame.changeState('2')

x=20
y=30

spatials=[]
rect=pygame.Rect(x,y,20,20)
mySpatial=dynSpatial(rect,2,BLUE)
mySpatial.addControl(repControl((200,200),(140,140),70))
handler=keyDownHandler([(K_s,moveBy_s),(K_w,changeState),(K_e,changeState2)]) #Setting keyhandlers in (key, action) pairs 
spatials.append(mySpatial)
states={'1':gameState(spatials,handler,WHITE),'2':gameState([],handler,BLUE)} #possible states
mygame = game(states,'1')
mygame.run()
