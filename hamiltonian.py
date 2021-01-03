import numpy as np

class table:

	def __init__(self,n):
		self.n=n
		self.array = []
		for x in range(n):
			self.array.append([])
			for y in range(n):
				self.array[x].append(case(n*x+y))

		self.array = np.array(self.array)

		if n%2==0:
			self.evengenerate()
	def index(self,x,y):
		return self.n*x+y
	def dindex(self,n):
		return n//self.n,n%self.n
	def evengenerate(self):
		n=self.n


		for y in range(1,n):
			self.array[0][y].cparent(self.array[0][y-1])

		for x in range(2,n-1):
			for y in range(0,n):
				if y%2==0:
					p = self.array[x+1][y]

				else: 
					p = self.array[x-1][y]
				self.array[x][y].cparent(p)

		for x in (1,n-1):
			for y in range(0,n,2):
				if x==1:

					p = self.array[x][y]
					p.cparent(self.array[x+1][y])
					c = self.array[x][y-1]
				else:

					p = self.array[x][y+1]
					p.cparent(self.array[x-1][y+1])
					c = self.array[x][y]
				if (not y in (0,n)) or x==n-1:
					c.cparent(p)


		self.array[0][0].cparent(self.array[1][0])
		self.array[1][n-1].cparent(self.array[0][n-1])



	def tolist(self):
		r = []

		for x in range(self.n):
			r.append([])
			for y in range(self.n):
				c = self.array[x][y]
				r[x].append((c.n,c.parent.n,c.child.n))
		return r

class case:
	def __init__(self,n):
		self.n=n
		if self.n >=0:
			self.parent = case(-1)
			self.child = case(-1)
	def cparent(self,p):
		self.parent=p
		p.child=self

