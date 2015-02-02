from baseobject import BaseObject

class Line(BaseObject):

    name = 'Line'

    def __init__(self,x1,y1,x2,y2,brush=' '):

        self.x1, self.y1, self.x2, self.y2 = x1,y1,x2,y2
        self.brush = brush

    def run(self,frame):
        frame.draw_line(self.x1, self.y1, self.x2, self.y2,self.brush)

        
