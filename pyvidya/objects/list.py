

from .baseobject import BaseObject

class List(BaseObject):

    def __init__(self,heading,x,y,list_items,indent = 4, denote = '-'):

        self.heading = heading
        self.x = x
        self.y = y
        self.things = list_items
        self.indent, self.denote = indent, denote


    def run(self,frame):
        y = self.y

        frame.text(self.x,self.y,self.heading)

        for thing in self.things:
            x = self.x + self.indent
            y -= 1
            frame.draw(x,y,self.denote)
            for char in thing:
                x += 1
                frame.draw(x,y,char)
