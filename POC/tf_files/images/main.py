
import os

home = "/home/ori/MEC2017/POC/tf_files/images/"

live = [f for f in os.listdir(home + "live") if isfile(join(home + "live", f))]
dead = [f for f in os.listdir(home + "dead") if isfile(join(home + "dead", f))]

print(live)
print(dead)
