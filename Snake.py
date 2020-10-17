from Food import *
from Neural import *
import copy
import random

DIR_UP = [0,-1]
DIR_DOWN = (0,1)
DIR_LEFT = (-1,0)
DIR_RIGHT = (1,0)

DIRECTIONS = [DIR_UP,DIR_RIGHT,DIR_DOWN,DIR_LEFT]

class Snake:
	def __init__(self):
		self.position = [[random.randint(5,15),random.randint(5,15)]]
		self.direction = DIR_UP
		self.food = Food()
		self.alive = True
		self.brain = NeuralNetwork(7,[32,64,32],4)
		self.lifetime = 0

	def update(self):
		self.lifetime += 1
		inputs = [len(self.position)/200]

		for p in self.position[0]:
			inputs.append(p/20)

		for p in self.food.position:
			inputs.append(p/20)

		for d in self.direction:
			inputs.append(d)

		out = list(self.brain.forward(inputs)[0])



		self.direction = DIRECTIONS[out.index(max(out))]

		newpos = [self.position[0][0]+self.direction[0],self.position[0][1]+self.direction[1]]

		if newpos in self.position or not newpos[0] in range(1,19) or not newpos[1] in range(1,19):
			self.alive = False

		self.position.insert(0,newpos)
		
		if self.position[0][0] == self.food.position[0] and self.position[0][1] == self.food.position[1]:
			self.food.randomize

		else:
			self.position.pop()



	def show(self,c,w,h):
		for body in self.position:
			r = c.create_rectangle(w/20*body[0],h/20*body[1],w/20*(body[0]+1),h/20*(body[1]+1),fill = 'green')
		self.food.show(c,w,h)

	def score(self):
		score = 60*len(self.position)
		score += 40 - (abs(self.position[0][0]-self.food.position[0])+abs(self.position[0][1]-self.food.position[1]))
		score += self.lifetime
		return score

	def copy(self):
		copy = Snake()
		copy.brain = self.brain.copy()
		return copy
