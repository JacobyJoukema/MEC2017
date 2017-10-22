from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse

from random import random, randint, uniform
import math

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

def randish_move():
    r = random() / 100
    theta = random() * 2 * math.pi
    x = math.cos(theta) * r
    y = math.sin(theta) * r
    return Pos(x,y)

def obscure_loc():
    r = random() / 100
    theta = random() * 2 * math.pi
    x = math.cos(theta) * r
    y = math.sin(theta) * r
    return Pos(x,y)

class Farm:
    def __init__(self, name, x, y):
        self.name = name
        self.pos = Pos(x, y)

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

def gen_swarm():
    long_a, lat_a = 43.076149, -80.125481
    long_b, lat_b = 43.168864, -79.930081

    lng = uniform(long_a, long_b)
    lat = uniform(lat_a, lat_b)

    s = Swarm()
    s.pos = Pos(lng, lat)
    s.mag = uniform(2, 10)
    return s

def fill_swarms(count):
    global swarms
    for i in range(count):
        swarms.append(gen_swarm())

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
    return ((math.fabs(a.x)-math.fabs(b.x))**2 + (math.fabs(a.y)-math.fabs(b.y))**2)**0.5

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
            s.mag += 5*random() - 0.2
            s.mag = max(s.mag, 0)
        
        # Update position, direction
        s.pos = s.pos + randish_move() + s.lean
        s.b = s.pos.y - s.pos.x * s.m

        s.life += 1

    swarms = [s for s in swarms if s.mag != 0]

def get_danger_level(dist, mag):
    ex = mag / dist

    # Mag goes from 0 to 80 approx (80 is full size swarm)
    # Dist: 0 to 0.3, 0.3 being max 

    danger = -1

    if (ex < 10):
        danger = 0
    elif (ex < 50):
        danger = 1
    elif (ex < 100):
        danger = 2
    elif (ex < 500):
        danger = 3
    elif (ex < 2000):
        danger = 4
    else:
        danger = 5

    f = open("danger.log", "a")
    f.write("Dist: " + str(dist) + ", Mag: " + str(mag) + ", Danger: " + str(danger) + "\n")
    f.close()

    return danger

def query_farm(farm_pos):
    global swarms
    max_danger = -1
    for s in swarms:
        p_ = farm_pos.y - s.minv * farm_pos.x
        x = (p_ - s.b) / (s.m + s.minv)
        y = s.m * x + s.b
        d = dist(Pos(x,y), farm_pos)
        danger = get_danger_level(d, s.mag)
        if (danger > max_danger):
            max_danger = danger
    return max_danger

fill_swarms(40)

points = {}
# X, Y, 0/1

ID = 0

def getID():
    global ID
    return ID

def incID():
    global ID
    ID += 1

def getSwarms():
    global swarms
    return swarms

class MainView(TemplateView):
    template_name = 'pests/index.html'

class PointApiView(View):
    def get(self, request):

        s = getSwarms()[randint(0, len(getSwarms())-1)]

        to_remove = []
        if (getID() >= 10):

            id_sel = randint(0, len(points.keys)-1)
            to_remove = [{
                'ID': points[points.keys[id_sel]].ID
                }]
            del points[id_sel]

        to_add = [{
            'lat': (obscure_loc() + s.pos).x,
            'long': (obscure_loc() + s.pos).y,
            'type': 0,
            'ID': getID()
            }]

        points[to_add['ID']] = to_add

        incID()
        update_swarms()

        return JsonResponse({
            'add': to_add
            'remove': to_remove
        })

# Create your views here.