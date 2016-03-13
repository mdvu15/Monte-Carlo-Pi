import math
import random

test = int(raw_input("Number of test: "))
inside = 0
for i in range(0,test):
  x = random.random()
  y = random.random()
  if math.sqrt((x-0.5)**2+(y-0.5)**2) <= 0.5:
    inside += 1

print inside/(test*0.25)


