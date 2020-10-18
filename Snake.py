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
	def __init__(self,food):
		self.position = [[10,10]]
		self.direction = DIR_UP
		self.food = food
		self.alive = True
		self.brain = NeuralNetwork(413,[24,24],4)
		self.lifetime = 0
		self.hunger = 0

	def update(self):
		self.lifetime += 1
		inputs = [len(self.position)/200]

		dnorth = self.position[0][1]
		dsouth = 20-dnorth
		dest = self.position[0][0]
		douest = 20-dest

		listd = [dnorth,dsouth,dest,douest]

		inputs.append(dnorth/20)
		inputs.append(dsouth/20)
		inputs.append(dest/20)
		inputs.append(douest/20)

		for x in range(20):
			for y in range(20):
				if [x,y] in self.position:
					inputs.append(1)
				elif [x,y] == self.food.position:
					inputs.append(0.5)
				else:
					inputs.append(0)


		mini = min(listd)

		inputs.append(mini/10)
		inputs.append(listd.index(mini)/4)

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
			self.food.randomize()
			self.hunger = 0
		else:
			self.position.pop()

		self.hunger += 1
		if self.hunger == 100*len(self.position):
			self.alive = False

	def show(self,c,w,h):
		for body in self.position:
			r = c.create_rectangle(w/20*body[0],h/20*body[1],w/20*(body[0]+1),h/20*(body[1]+1),fill = 'green')
		self.food.show(c,w,h)

	def score(self):
		score = 60*len(self.position)
		score += 40 - (abs(self.position[0][0]-self.food.position[0])+abs(self.position[0][1]-self.food.position[1]))
		score += max(0,self.lifetime-5*self.hunger) ** 2

		return score

	def copy(self):
		copy = Snake(self.food)
		copy.brain = self.brain.copy()
		return copy
