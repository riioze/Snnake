import random

class Food:
	def __init__(self):
		self.position = [0,0]
		self.randomize()

	def randomize(self):
		self.position[0] = random.randint(2,18)
		self.position[1] = random.randint(2,18) 

	def show(self,c,w,h):
		x,y = self.position
		r = c.create_oval(w/20*x,h/20*y,w/20*(x+1),h/20*(y+1),fill = 'red')