from baseanimation import BaseAnimation
import time

class Appear(BaseAnimation):

	def __init__(self,obj,delay):
		self.obj = obj
		self.delay = delay

	def run(self,frame):
		self.obj.run(frame)
		time.sleep(self.delay)
