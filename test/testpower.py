import numpy as np
import matplotlib as plt

# distance
def distance(x, y):
  dist = np.linalg.norm(x - y)
  return dist

# c func
def c(d, g):
  ret = np.power(d-g, 2)
  return ret

test1d = np.array([0, 5])
test1g = np.array([4, 7])
test1 = c(test1d, test1g)
print(f"c: {test1}")

disttest1 = distance(test1g, test1d)
disttest2 = distance(test1g, test1g)

print(f"disttest1: {disttest1}")
print(f"disttest2: {disttest2}")
