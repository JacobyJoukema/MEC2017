
from random import rand, randint
import math

class Pos:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Pos(self.x + other.x, self.y + other.y)

def randish_move():
	r = rand()
	theta = rand() * 2 * math.pi
	x = math.cos(theta) * r
	y = math.sin(theta) * r
	return Pos(x,y)

class Swarm:
	def __init__(self):
		self.pos = Pos(0,0)
		self.mag = 0
		self.life = 0
		self.lean = randish_move()
		self.lean.x /= 2
		self.lean.y /= 2 
		self.m = self.lean.y / self.lean.x
		self.minv = -1 / self.m
		self.b = 0

swarms = []

def read_farms():
	f = open("farms", "r")
	farms = [i.split() for i in f.readlines()]
	f.close()
	for i in farms:
		i[0] = i[0].replace("_", " ")
	return farms

def add_farm(farms, name, x ,y):
	farms.append([name, x, y])

def save_farms(farms):
	f = open("farms", "w")
	for fa in farms:
		f.write(fa[0].replace(" ", "_") + " " + str(fa[1]) + " " + str(fa[2]) + "\n")
	f.close()

def dist(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def update_swarms():
	global swarms

	# Assuming 120 updates/min
	# Swarm should live for about 2 minutes -> 200 life
	for s in swarms:
		if (s.life > 200):

			# Should start dying off
			s.mag *= 0.8
			if (s.mag < 1): # Outright kill small enough swarms
				s.mag = 0
		else:
			# Keep growing
			s.mag += rand() - 0.2
			s.mag = max(swarm.mag, 0)
		
		# Update position, direction
		s.pos = s.pos + randish_move() + s.leans
		s.b = s.pos.y - s.pos.x * s.m

		s.life += 1

	swarms = [s for s in swarms if s.mag != 0]

def query_farm(farm_pos):
	global swarms
	for s in swarms:
		p_ = farm_pos.y - s.minv * farm_pos.x
		x = (p_ - s.b) / (s.m + s.minv)
		y = s.m * x + s.b
		d = dist(Pos(x,y), farm_pos)
		












