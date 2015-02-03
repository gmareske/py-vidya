# list animation
from baseanimation import BaseAnimation
import time

class ListDraw(BaseAnimation):

	name = 'List Draw'
	
	def __init__(self,x,y,heading,list_items,delay,denote='-',indent=4,scroll=True,inbetween=0.7):
		self.x,self.y,self.heading,self.list_items,self.delay = x,y,heading,list_items,delay
		self.denote,self.indent,self.scroll,self.inbetween = denote,indent,scroll,inbetween

	def run(self,frame):
		x,y = self.x,self.y
		if self.scroll:
			self.file_right(frame,self.heading,x,y,self.delay)
		else:
			frame.text(x,y,self.heading)
			frame.display()

		for thing in self.list_items:
			x = self.x + self.indent
			time.sleep(self.inbetween)
			y -= 1
			frame.draw(x,y,self.denote)
			x += 1
			if self.scroll:
				self.file_right(frame,thing,x,y,self.delay)
			else:
				frame.text(x,y,thing)
				frame.display()

