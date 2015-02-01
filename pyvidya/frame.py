# Frame object serves as a wrapper to contain
# static objects and animations


import drawframe
import time
import os

class Frame(object):

	def __init__(self,name,delay,pre_delay=0,height=24,width=80):
		self.delay = delay
		self.pre_delay = pre_delay
		self.height = height
		self.width = width
		# container for objects on the Frame
		self.objects = []
		# container for animations
		self.anims = []
		self.base = drawframe.DrawFrame(height,width)


	def render(self):
		# call .run() on each of this frame's objects
		self.base = drawframe.DrawFrame(self.height,self.width)
		for o in self.objects:
			o.run(self.base)

	def run(self):
		self.base.display()
		time.sleep(self.pre_delay)
		if len(self.anims):
			for a in self.anims:
				a.run(self.base)

		self.render()
		time.sleep(self.delay)
