from baseanimation import BaseAnimation

class BoxDraw(BaseAnimation):

	name = 'Box Draw'

	def __init__(self,x,y,height,width,border,delay):
		self.x, self.y, self.height, self.width = x,y,height,width
		self.delay = delay
		self.horiz = self.make_line(border,width-1)
		self.vert = self.make_line(border[::-1],height-1)
		self.height -= 1
		self.width -= 1

	def run(self,frame):
		self.file_right(frame,self.horiz,self.x, self.y + self.height,self.delay)
		self.file_down(frame,self.vert, self.x + self.width, self.y + self.height,self.delay)
		self.file_left(frame,self.horiz, self.x + self.width, self.y, self.delay)
		self.file_up(frame,self.vert, self.x,self.y,self.delay)