# Python base class for Frame, DrawFrame
# contains all of the methods used for drawing on a two-dimensional array

class DrawFrame(object):

	# name: Name of the frame
	# delay: Time in seconds slept after animations are played
	# pre_delay: Time in seconds slept before animations are played
	# height: height of the frame
	# width: width of the frame
	# Both heigh and width are set for the default Windows command prompt of 25*80 characters

	newline = ''

	def __init__(self,name,delay,pre_delay=0,height=24,width=80):
		self.name = name
		self.delay = delay
		self.pre_delay = pre_delay
		self.height = height
		self.width = width

		# the actual two-dimensional array
		self.base = self.blankframe(height,width)

	# UTILITY METHODS

	def blankframe(self,height,width):
		# returns a blank multidimensional array of ' ' characters
		return [[' ' for n in range(0,width)] for x in range(0,height)]

	def display(self):
		# loads each line in the frame into a temporary buffer
		tempframe = []
		for line in self.base:
			tempframe.append(''.join(line))
		# then prints the buffer all at once
		print(self.newline.join(tempframe))

	def graphable(self,x,y):
		# if both x and y are within the frame, return true
		if x <= self.width and x > 0 and y <= self.height and y > 0:
			return True
		else:
			#TODO change so it fails silently or just logs error
			print('ERROR: ({0},{1}) is out of the frame'.format(x,y))
			return False

	# DRAWING METHODS

	def draw(self,x,y,brush=' ',overwrite=True):
		if self.graphable(x,y):
			if overwrite:
				# set the corresponding element at [x][y] in the frame to brush
				# y is inverted so the frame acts as Quadrant 1 of a coord graph
				# if it wasn't, it would be similar to Quadrant 4 of a coord graph
				self.base[-1 * y][x-1] = brush
			elif not overwrite and not brush == ' ':
				self.base[-1 * y][x-1] = brush

		return self.base

	def horizontal_line(self,y,xstart,xend,brush=' '):
    	for x in range(xstart,xend):
        	self.draw(x,y,brush)

	def vertical_line(self,x,ystart,yend,brush=' '):
    	for y in range(ystart,yend):
        	self.draw(x,y,brush)