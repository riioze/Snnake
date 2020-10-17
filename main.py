from Neural import *
from Snake import *
import tkinter as tk
import time
import random

root = tk.Tk()

WIDTH = 500
HEIGHT = 500
POPSIZE = 25


canvas = tk.Canvas(root,width = WIDTH,height = HEIGHT,bg = 'black')
canvas.pack()



snakes = []
for x in range(POPSIZE):
	snakes.append(Snake())

isonealive = True


while True:

	camera = random.choice(snakes)

	while isonealive:

		canvas.delete(tk.ALL)

		isonealive = False
		for snake in snakes:
			
			if snake.alive:
				snake.update()

				isonealive = True

		snake.show(canvas,WIDTH,HEIGHT)



		root.update()

		# time.sleep(0.1)

	pool = []

	for snake in snakes:
		for x in range(snake.score()):
			pool.append(snake.copy())

	new = []
	for x in range(POPSIZE):
		choosed = random.choice(pool)
		choosed.brain.mutate()
		pool.remove(choosed)
		new.append(choosed)

	snakes = new



	isonealive = True





# root.mainloop()