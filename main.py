from Neural import *
from Snake import *
import tkinter as tk
import time
import random
from math import inf
import matplotlib.pyplot as plt

root = tk.Tk()
bestscores = {'Gen' : [], 'best' : [],'popsize' : []}
WIDTH = 500
HEIGHT = 500
POPSIZE = 50

CAMERAMODE = False

SHOW_EVERY = 10

canvas = tk.Canvas(root,width = WIDTH,height = HEIGHT,bg = 'black')
canvas.pack()

food = Food()

gennum = 0

snakes = []
for x in range(POPSIZE):
	snakes.append(Snake(food))

isonealive = True


for feen in range(2000):
	gennum+=1

	camera = random.choice(snakes)

	while isonealive:

		canvas.delete(tk.ALL)

		isonealive = False
		for snake in snakes:
			
			if snake.alive:
				snake.update()

				isonealive = True

				if (not CAMERAMODE or snake == camera) and gennum % SHOW_EVERY == 0:
					snake.show(canvas,WIDTH,HEIGHT)
					root.update()








	pool = []
	best = None
	bestscore = -100000
	for snake in snakes:
		if snake.score() > bestscore:
			bestscore = snake.score()
			best = snake
		for x in range(int(1.4245*snake.score()**0.98475/100)):
			pool.append(snake.copy())

	for snake in pool:
		snake.brain.mutate()

	snakes = pool

	print(f'Generation num {gennum} : best score is {bestscore}, next population size : {len(snakes)}')
	bestscores['Gen'].append(gennum)
	bestscores['best'].append(bestscore)
	bestscores['popsize'].append(len(snakes))


	isonealive = True

	food.randomize()


plt.plot(bestscores['Gen'],bestscores['best'],label = "best")
plt.plot(bestscores['Gen'],bestscores['popsize'],label = "popsize")


plt.legend(loc = 4)
plt.show()


# root.mainloop()