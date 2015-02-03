# textscroll animations
from baseanimation import BaseAnimation

class TextScroll(BaseAnimation):

	name = 'Text Scroll'

	def __init__(self,x,y,text,delay,direction='right'):
		self.x, self.y, self.text, self.delay = x,y,text,delay
		self.direction = direction

	def run(self,frame):
		direction = self.direction
		if direction == 'right':
			self.file_right(frame,self.text,self.x,self.y,self.delay)
		elif direction == 'left':
			self.file_left(frame,self.text,self.x,self.y,self.delay)
		elif direction == 'up':
			self.file_up(frame,self.text,self.x,self.y,self.delay)
		elif direction == 'down':
			self.file_down(frame,self.text,self.x,self.y,self.delay)
