import pygame,sys
from spatials import *
from pygame.locals import *
from settings import *
from inputHandlers import baseHandler

class gameState():
    def __init__(self,spatials,handler,color = WHITE):                            
        """  """
        self.spatials=spatials
        self.inputHandler=handler
        self.isRunning=False
        self.color=color
        
        
    def setSurface(self,surf):
        self.surf=surf
    def run(self,fpsClock,FPS):
        self.isRunning=True
        while self.isRunning:            
            self.background_draw()
            for event in pygame.event.get():
                self.inputHandler.handle_input(event)            
            self.update()
            self.draw()
            self.HUD_draw()
            pygame.display.update()
            fpsClock.tick(FPS)
    def stop(self):
        self.isRunning=False
    def update(self):
        for s in self.spatials:
            s.update()    
    def background_draw(self):
        self.surf.fill(self.color)
        pass
    def HUD_draw(self):
        pass
    
    def draw(self):
        for s in self.spatials:
            s.draw(self.surf)
               
