# image object

from baseobject import BaseObject

class Image(BaseObject):

	def __init__(self,x,y,path):
		self.x = x
		self.y = y
		self.path = path
		self.name = 'Image: {}'.format(path)

		self.open_img(path)


	def open_img(self,path):
		try:
			file = open(path,mode='r')
			self.valid = True
		except:
			print("Couldn't open {}, file doesn't exist".format(path))
			self.valid = False

		if self.valid:
			self.parse(file)

	def parse(self,file):
		lines = []
		for line in file:
			lines.append(line.rstrip('\n'))

		self.img = lines
		file.close()

	def run(self,frame):
		y = self.y
		for line in self.img:
			x = self.x
			for char in line:
				frame.draw(x,y,char)
				x += 1

			y -= 1