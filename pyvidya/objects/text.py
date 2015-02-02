from baseobject import BaseObject
class Text(BaseObject):

    name = 'Text'
    help =  '''
        TextObjects are areas of text on the frame.

        PARAMETERS:
            x = REQUIRED. x coordinate of the first character in the text
            y = REQUIRED. y coordinate of the first character in the text
            text = REQUIRED. characters to display
            wrap = DEFAULTS to TRUE. whether the text should wrap around if too long
            wrapmax = DEFAULTS to 78. the length at which the text wraps to a new line

        '''

    

    
    def __init__(self,x,y,text,wrap=True,wrapmax=78):
        self.x, self.y, self.text, self.wrap, self.wrapmax = x,y,text,wrap,wrapmax


    def run(self,frame):
        frame.text(self.x,self.y,self.text,self.wrap,self.wrapmax)