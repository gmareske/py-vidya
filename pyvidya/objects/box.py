from baseobject import BaseObject

class Box(BaseObject):
	name = 'Box'
	help = ''' '''

	def __init__(self,x,y,height,width,brush=' ',fill=False):
		self.x, self.y, self.height, self.width = x,y,height,width
		self.brush = brush
		self.fill = fill


	def run(self,frame):
		frame.box(self.x,self.y,self.height,self.width,self.brush,self.fill)
