import hamiltonian as hml
import copy
import random
import food

DIR_UP = (0,-1)
DIR_DOWN = (0,1)
DIR_LEFT = (-1,0)
DIR_RIGHT = (1,0)

def setheight(a,b):
	global th,tw
	th,tw=a,b
	food.seth(a,b)

DIRECTIONS = [DIR_UP,DIR_RIGHT,DIR_DOWN,DIR_LEFT]

class Snake:
	def __init__(self,food):
		self.position = [(1,6)]
		self.direction = DIR_UP
		self.food = food
		self.alive = True
		self.hgrid = hml.table(th)
		self.lifetime = 0
		self.hunger = 0

	def update(self):
		self.lifetime += 1
		

		x,y = self.position[0]
		togox,togoy = self.hgrid.dindex(self.hgrid.array[x][y].child.n)

		self.direction = togox-x,togoy-y

		newpos = (self.position[0][0]+self.direction[0],self.position[0][1]+self.direction[1])

		if newpos in self.position or  newpos[0] in (-1,th+1) or newpos[1] in (-1,tw+1):
			self.alive = False

		self.position.insert(0,newpos)
		
		if self.position[0][0] == self.food.position[0] and self.position[0][1] == self.food.position[1]:
			allp = []
			for x in range(th):
				for y in range(tw):
					if not (x,y) in self.position:
						allp.append((x,y))

			self.food.randomize(allp)

		else:
			self.position.pop()

		if len(self.position)==(th*tw)-1:
			return 'win'

	def show(self,c,w,h):

		for body in self.position:
			r = c.create_rectangle(w/th*body[1],h/tw*body[0],w/th*(body[1]+1),h/tw*(body[0]+1),fill = 'green')

		self.food.show(c,w,h)

	def score(self):
		score = 60*len(self.position)
		score += 40 - (abs(self.position[0][0]-self.food.position[0])+abs(self.position[0][1]-self.food.position[1]))
		score += self.lifetime

		return score

	def copy(self):
		copy = Snake(self.food)
		copy.brain = self.brain.copy()
		return copy
