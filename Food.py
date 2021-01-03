import random

def seth(a,b):
	global th,tw
	th,tw=a,b

class Food:
	def __init__(self,p):
		self.position = (0,0)
		self.randomize(p)

	def randomize(self,posible):
		x,y = random.choice(posible)
		self.position = x,y

	def show(self,c,w,h):
		x,y = self.position
		r = c.create_oval(w/tw*y,h/th*x,w/tw*(y+1),h/th*(x+1),fill = 'red')