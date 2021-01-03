from food import *
from Snake import *
import tkinter as tk
import time
import random
from math import inf
import matplotlib.pyplot as plt

root = tk.Tk()
bestscores = {'Gen' : [], 'best' : [],'popsize' : []}
WIDTH = 600
HEIGHT = 600
POPSIZE = 1
th,tw=20,20

setheight(th,tw)
CAMERAMODE = False

SHOW_EVERY = 10

canvas = tk.Canvas(root,width = WIDTH,height = HEIGHT,bg = 'black')
canvas.pack()

possible = []
for x in range(th):
	for y in range(tw):
		possible.append((x,y))
food = Food(possible)

snakes = []
for x in range(POPSIZE):
	snakes.append(Snake(food))

isonealive = True


for feen in range(1):


	camera = random.choice(snakes)

	while isonealive:
		# time.sleep(0.1)
		canvas.delete(tk.ALL)

		isonealive = False
		for snake in snakes:
			
			if snake.alive:
				r = snake.update()



				isonealive = True



				snake.show(canvas,WIDTH,HEIGHT)
				root.update()

				if r=='win':
					snake.show(canvas,WIDTH,HEIGHT)
					print('win')
					root.mainloop()






# root.mainloop()