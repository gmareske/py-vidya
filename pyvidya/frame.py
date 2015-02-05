# Frame object serves as a wrapper to contain
# static objects and animations


import drawframe
import time
import os

class Frame(object):

	def __init__(self,name,delay,pre_delay=0,height=23,width=80):
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
		if len(self.anims) > 0:
			for a in self.anims:
				a.run(self.base)

		self.render()
		time.sleep(self.delay)

	def add_object(self,obj):
		self.objects.append(obj)
		self.render()

	def add_anim(self,anim):
		self.anims.append(anim)

	def list_objects(self):
		print('Objects on frame {}'.format(self.name))
		num = 1
		for o in self.objects:
			print('{0}: {1} at ({2}, {3})'.format(num,o.name,o.x,o.y))
			num += 1

	def list_anims(self):
		print('Animations on frame {}'.format(self.name))
		num = 1
		for a in self.anims:
			print('{0}: {1}'.format(num,a.name))
