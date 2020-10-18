import numpy as np
import copy as c
import random



def ReLU(x):
	return np.maximum(0,x)

def dReLU(a):
	r = np.zeros((len(a),len(a[0])))
	for x in range(len(a)):
		for y in range(len(a[x])):
			if a[x][y] == 0:
				r[x][y] = 0
			else: 
				r[x][y] = 1
	return r





class Layer:
	def __init__(self,ninputs,nneurons):
		self.ninputs = ninputs
		self.nneurons = nneurons
		self.weights = 0.10*np.random.randn(ninputs,nneurons)
		self.biases = np.ones((1,nneurons))
		

	def forward(self,inputs):
		
		self.output = np.dot(inputs,np.array(self.weights))+self.biases
		return self.output

	def copy(self):
		copy = Layer(self.ninputs,self.nneurons)

		for x in range(len(self.weights)):
			copy.weights[x] = c.deepcopy(self.weights[x])

		copy.biases = c.deepcopy(self.biases)

		return copy

	def mutate(self,learning):

		for b in self.biases:
			if random.uniform(0,1) <= learning:
				b += random.uniform(-learning,learning)

		for wa in self.weights:
			for wb in wa:
				wb+= random.uniform(-learning,learning)




class NeuralNetwork:
	def __init__(self,ninputs,listnhidden,noutputs):
		self.ninputs = ninputs
		self.listnhidden = listnhidden
		self.noutputs = noutputs
		self.learning = 0.1
		self.hidden = [Layer(ninputs,listnhidden[0])]
		for x in range(len(listnhidden)-1):
			self.hidden.append(Layer(listnhidden[x],listnhidden[x+1]))
		self.output = Layer(listnhidden[-1],noutputs)

	def forward(self,inputs):
		outputs = inputs
		for x in range(len(self.hidden)):
			outputs = ReLU(self.hidden[x].forward(outputs))
		self.outputs = self.output.forward(outputs)
		return self.outputs

	def copy(self):
		# if random.uniform(0,10) < self.learning:
		# 	self.listnhidden[random.randrange(len(self.listnhidden))] += 1

		# if random.uniform(0,100) < self.learning:
		# 	self.listnhidden.append(random.randint(7,13))

		copy = NeuralNetwork(self.ninputs,self.listnhidden,self.noutputs)
		for x in range(len(self.hidden)):
			copy.hidden[x] = self.hidden[x].copy()
		copy.output = self.output.copy()

		return copy

	def mutate(self):
		for x in range(len(self.hidden)):
			self.hidden[x].mutate(self.learning)