# pause animation, to create a pause in the movie
from baseanimation import BaseAnimation

class Pause(BaseAnimation):

	name = 'Pause'

	def __init__(self,delay):
		self.delay = delay

	def run(self,frame):
		# kind of anticlimactic isn't it
		time.sleep(self.delay)
