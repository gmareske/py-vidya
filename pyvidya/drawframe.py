# Python base class for Frame, DrawFrame
# contains all of the methods used for drawing on a two-dimensional array
import copy

class DrawFrame(object):

	# name: Name of the frame
	# delay: Time in seconds slept after animations are played
	# pre_delay: Time in seconds slept before animations are played
	# height: height of the frame
	# width: width of the frame
	# Both heigh and width are set for the default Windows command prompt of 25*80 characters

	newline = ''

	def __init__(self,height=23,width=80):
		# the actual two-dimensional array
		self.height = height
		self.width = width
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

	def point(self,x,y):
		# returns the element of the frame at [x][y]
		if self.graphable(x,y):
			return self.base[-1*y][x-1]

	def copy(self):
		return copy.deepcopy(self)

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
		for x in range(xstart,xend+1):
			self.draw(x,y,brush)

	def vertical_line(self,x,ystart,yend,brush=' '):
		for y in range(ystart,yend+1):
			self.draw(x,y,brush)

	def draw_line(self,x0,y0,x1,y1,brush=' '):
		# bresenham's line algorithm
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x,y = x0,y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2.0
			while x != x1:
				self.draw(x,y,brush)
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx

		else:
			err = dy / 2.0
			while y != y1:
				self.draw(x,y,brush)
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy

		self.draw(x,y)

	def box(self,xstart,ystart,height,width,brush=' ',fill=False):
		# bl is bottom left corner of box
		# tl is top left corner of box
		bl = xstart + width - 1
		tl = ystart + height - 1
		self.horizontal_line(ystart, xstart, bl, brush)
		self.vertical_line(xstart, ystart, tl, brush)
		self.horizontal_line(tl, xstart, bl, brush)
		self.vertical_line(bl, ystart, tl, brush)
		if fill:
			for x in range(xstart+1,xstart+width):
				self.vertical_line(x,ystart,tl,brush)

	def write(self,xstart,ystart,arr,overwrite=True):
		# write() takes a multidimensional array, arr, as an input
		# and places it at the coordinates xstart,ystart
		# xstart and ystart specifiy the top left corner of the array
		y = ystart
		for line in arr:
			x = xstart
			for i in line:
				self.draw(x,y,i,overwrite)
				x += 1
			
			y -= 1

	def text(self,xstart,ystart,string,wrap=True,wrapmax=78,draw=True):
		string.rstrip('\n')
		text = []
		if wrap:
			if len(string) < wrapmax:
				text = [string]
			else:
				while len(string) > wrapmax:
					text.append(string[0:wrapmax-1])
					string = string[wrapmax:]
				text.append(string)
		else:
			text = [string]
		# optional argument to have the text returned to the caller 
		if draw:
			self.write(xstart,ystart,text)
		else:
			return text
