# the ultimate wrapper: Movie class

class Movie(object):

	def __init__(self,name):

		self.name = name
		self.frames = []

	def add_frame(self,frame):
		self.frames.append(frame)

	def list_frames(self):
		for frame in self.frames:
			num = 1
			print('{0}: {1}'.format(num,frame.name))

	def get_frame(self,num):
		return self.frames[num]
