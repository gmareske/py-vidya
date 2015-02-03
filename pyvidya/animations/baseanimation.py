# base class for animations

import time

#contain methods needed for animations
class BaseAnimation(object):

	characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}:-_+='
	char_length = len(characters)

	def file_right(self,frame,text,x,y,delay):
		# displays a line of text, one character at a time
		for char in text:
			frame.draw(x,y,char)
			x += 1 
			time.sleep(delay)

	def file_left(self,frame,text,x,y,delay):
		# as above, but reversed
		for char in text:
			frame.draw(x,y,char)
			x -= 1
			time.sleep(delay)

	def file_down(self,frame,text,x,y,delay):
		for char in text:
			frame.draw(x,y,char)
			y -= 1
			time.sleep(delay)

	def file_up(self,frame,text,x,y,delay):
		for char in text:
			frame.draw(x,y,char)
			y += 1
			time.sleep(delay)