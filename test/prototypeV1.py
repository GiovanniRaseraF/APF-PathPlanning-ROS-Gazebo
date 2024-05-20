#
# Authors: 
#   - Giovanni Rasera
#   - Diletta Giabardo
#

import numpy as np
import matplotlib.pyplot as plt
import time
import math

#drone
drone = np.array([1, 14])
goal = np.array([40, 20])

s = 15
r = 0.5

# epsilon
epsilon = 1

# field
x = np.arange(-0,50,1)
y = np.arange(-0,50,1)
X, Y = np.meshgrid(x,y)
delx = np.zeros_like(X)
dely = np.zeros_like(Y)

# plotting
plt.ion()

# IMPORTANT
# This function draws and creates the field
# Just for testing and quick prototype dev
#
def draw():
  # obstacle
  obstacle = np.array([20, 20])

  # creazione del potential field
  for i in range(len(x)):
    for j in range(len(y)):
      # finding the goal distance and obstacle distance
      d_goal = np.sqrt((goal[0]-X[i][j])**2 + ((goal[1]-Y[i][j]))**2)
      d_obstacle = np.sqrt((obstacle[0]-X[i][j])**2 + (obstacle[1]-Y[i][j])**2)

      #finding theta correspoding to the goal and obstacle 
      theta_goal = np.arctan2(goal[1] - Y[i][j], goal[0] - X[i][j])
      theta_obstacle = np.arctan2(obstacle[1] - Y[i][j], obstacle[0] - X[i][j])

      if d_obstacle < r:
        delx[i][j] = np.sign(np.cos(theta_obstacle)) +0
        dely[i][j] = np.sign(np.cos(theta_obstacle)) +0
      elif d_obstacle>r+s:
        delx[i][j] = 0 + (50 * s * np.cos(theta_obstacle))
        dely[i][j] = 0 + (50 * s * np.sin(theta_goal))
      elif d_obstacle<r+s :
        delx[i][j] = -120 * (s+r-d_obstacle) * np.cos(theta_obstacle)
        dely[i][j] = -120 * (s+r-d_obstacle) * np.sin(theta_obstacle) 
      if d_goal <r+s:
        if delx[i][j] != 0:
          delx[i][j]  += (50 * (d_goal-r) * np.cos(theta_goal))
          dely[i][j]  += (50 * (d_goal-r) * np.sin(theta_goal))
        else:
          delx[i][j]  = (50 * (d_goal-r) * np.cos(theta_goal))
          dely[i][j]  = (50 * (d_goal-r) * np.sin(theta_goal))
        
      if d_goal>r+s:
        if delx[i][j] != 0:
          delx[i][j] += 50 * s * np.cos(theta_goal)
          dely[i][j] += 50 * s * np.sin(theta_goal)
        else:
          delx[i][j] = 50 * s * np.cos(theta_goal)
          dely[i][j] = 50 * s * np.sin(theta_goal)

  fig, ax = plt.subplots(figsize=(10, 10))
  ax.quiver(X, Y, delx, dely)

  #obstacle
  ax.add_patch(plt.Circle(obstacle, r*2, color='y'))
  ax.annotate("Obstacle", xy=obstacle, fontsize=8, ha="center")

  #goal
  ax.add_patch(plt.Circle(goal, r, color='m'))
  ax.annotate("Goal", xy=goal, fontsize=1, ha="center")

  #drone
  ax.add_patch(plt.Circle(drone, r, color='r'))
  ax.annotate("Drone", xy=drone, fontsize=1, ha="center")

  fig.canvas.draw()
  fig.canvas.flush_events()

# distance
def distance(x, y):
  dist = np.linalg.norm(x - y)
  return dist

def c(d, g):
  ret = np.power(d-g, 2)
  return ret

# distance(x, y) = || x - y ||

# movimento a caso
while distance(drone, goal) > epsilon:
  # 1. compute the gradient decent of the cost function
  ck = np.array([0, 0])
  ck[0] = c(drone, goal)[0] # / dx # dx of c(xk)
  ck[1] = c(drone, goal)[1] # / dy # dy of c(xk)

  # 2. take the oppotite direction
  Nck = -ck
  Dk = Nck / distance(ck, np.array([0, 0]))

  print(f"Dk: {Dk}, Nk: {Nck}")

  # 2.1 fake movement
  droneGridPos = np.array([math.floor(drone[0]), math.floor(drone[1])])
  forceOnDrone = np.array([
    delx[droneGridPos[0]][droneGridPos[1]], 
    dely[droneGridPos[0]][droneGridPos[1]]
  ])
  print(f"droneGridPos: {droneGridPos}")
  print(f"forceOnDrone: {forceOnDrone}")

  drone = drone - Dk

  # 3. compute the time step
  # 4. update drone position

  # IO
  draw()

  # input to slow execution
  a = input()

  # close to prevent opening
  plt.close()
  