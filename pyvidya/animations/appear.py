# appear animation 
from baseanimation import BaseAnimation

class Appear(BaseAnimation):

	name = 'Appear'

	def __init__(self,obj,delay):
		self.delay = x,y,delay
		self.object = obj

	def run(self,frame):
		self.object.run(frame)
		frame.display()
		time.sleep(self.delay)