import pygame,sys
from spatials import *
from pygame.locals import *
from settings import *
from inputHandlers import baseHandler
class game():
    def __init__(self,states,startState,width = WINDOWWIDTH,height = WINDOWHEIGHT):        
        pygame.init()
        pygame.key.set_repeat(100, 300)
        self.fpsClock=pygame.time.Clock()
        self.surf=pygame.display.set_mode((width, height))
        self.states=states
        self.currState=self.states[startState]
        for x in states.values():
            x.setSurface(self.surf)
    def run(self):
        while True:
            self.currState.run(self.fpsClock,FPS)
    def changeState(self,stateName):
        if not self.states[stateName].isRunning:
            self.currState.stop()            
            self.currState=self.states[stateName]            

