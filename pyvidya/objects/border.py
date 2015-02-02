from .baseobject import BaseObject

class Border(BaseObject):

	name = 'Border'
	x = 1
	y = 1
	height = 24
	width = 80

	help = '''
	Border Object:
		Parameters:
		brush = REQUIRED string, the character to use for the border
		fill = DEFAULT False, whether the screen should be filled with brush
	'''

	def __init__(self,brush,fill=False):
		self.brush = brush
		self.fill = fill

	def run(self,frame):
		frame.box(self.x,self.y,self.height,self.width,self.brush,self.fill)

