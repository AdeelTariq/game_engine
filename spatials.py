import settings
import controls
import pygame
time_interval=0.001*1000/settings.FPS

    
class spatial():
    def __init__(self,rect, z, color):
        self.posZ= z
        self.rect = rect
        self.color = color
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, 0)
    def on_screen(self, minX, maxX, minY, maxY):
        if self.rect.right<minX or self.rect.left>maxX :
            return False
        if self.rect.top<minY or self.rect.bottom>maxY :
            return False
        return True
    def update(self):
        pass
    def getX(self):
        return self.rect.centerx
    def getY(self):
        return self.rect.centery
    def moveTo(self,point):
        self.rect=self.rect.move(point)
class dynSpatial(spatial):    
        def __init__(self,rect,z, color):
            spatial.__init__(self,rect,z,color)            
            self.v=(0,0)
            self.a=(0,0)            
            self.controls=[]
        def addControl(self,control):
            control.setSpatial(self)
            self.controls.append(control)
        def update(self):
            if not (self.a[0]==0 and self.a[1]==0):
                newVx=self.v[0]+self.a[0]*time_interval
                newVy=self.v[1]+self.a[1]*time_interval
                self.v=(newVx,newVy)            
            self.rect.x+=self.v[0]*time_interval
            self.rect.y+=self.v[1]*time_interval
            for control in self.controls:
                control.update()
        def stop(self):
            self.v=(0,0)
            self.a=(0,0)


class button():
    def __init__(self,rect,text,textSize,action):
        self.rect=rect
        self.text=text
        self.textSize=textSize
        self.action=action
        self.focus=False        
    def activate(self):
        self.action()    
    def draw(self,surface):
        pass
    def isOnButton(self, point):
        return self.rect.collidepoint(point)
        
                    

