
class Swarm:
	def __init__(self):
		self.loc = [0,0]
		self.mag = 0

class Crop:
	def __init__(self):
		self.loc = [0,0]
		self.mag = 0

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

a = read_farms()
for i in a:
	print i

add_farm(a, "My Happy Place", 1, 1)
for i in a:
	print i

save_farms(a)