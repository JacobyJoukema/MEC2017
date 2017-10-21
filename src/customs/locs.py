
class Swarm:
	def __init__(self):
		self.loc = [0,0]
		self.mag = 0

class Crop:
	def __init__(self):
		self.loc = [0,0]
		self.mag = 0

def get_farms():
	f = open("farms", "r")
	farms = [i.split() for i in f.readlines()]
	f.close()
	for i in farms:
		i[0] = i[0].replace("_", " ")
	return farms

a = get_farms()
for i in a:
	print i

