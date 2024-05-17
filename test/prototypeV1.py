#
# Authors: 
#   - Giovanni Rasera
#   - Diletta Giabardo
#

import numpy as np
import matplotlib.pyplot as plt
import time

#drone
drone = np.array([10, 10])
goal = np.array([40, 40])

s = 15
r=2

# epsilon
epsilon = 1

# plotting
plt.ion()

# IMPORTANT
# This function draws and creates the field
# Just for testing and quick prototype dev
#
def draw():
  x = np.arange(-0,50,1)
  y = np.arange(-0,50,1)

  # obstacle
  obstacle = np.array([20, 20])

  # field
  X, Y = np.meshgrid(x,y)

  delx = np.zeros_like(X)
  dely = np.zeros_like(Y)

  # creazione del potential field
  for i in range(len(x)):
    for j in range(len(y)):
      # finding the goal distance and obstacle distance
      d_goal = np.sqrt((goal[0]-X[i][j])**2 + ((goal[1]-Y[i][j]))**2)
      d_obstacle = np.sqrt((obstacle[0]-X[i][j])**2 + (obstacle[1]-Y[i][j])**2)

      #finding theta correspoding to the goal and obstacle 
      theta_goal= np.arctan2(goal[1] - Y[i][j], goal[0]  - X[i][j])
      theta_obstacle = np.arctan2(obstacle[1] - Y[i][j], obstacle[0]  - X[i][j])

      if d_obstacle < r:
        delx[i][j] = np.sign(np.cos(theta_obstacle)) +0
        dely[i][j] = np.sign(np.cos(theta_obstacle))  +0
      elif d_obstacle>r+s:
        delx[i][j] = 0 +(50 * s *np.cos(theta_obstacle))
        dely[i][j] = 0 + (50 * s *np.sin(theta_goal))
      elif d_obstacle<r+s :
        delx[i][j] = -120 *(s+r-d_obstacle)* np.cos(theta_obstacle)
        dely[i][j] = -120 * (s+r-d_obstacle)*  np.sin(theta_obstacle) 
      if d_goal <r+s:
        if delx[i][j] != 0:
          delx[i][j]  += (50 * (d_goal-r) *np.cos(theta_goal))
          dely[i][j]  += (50 * (d_goal-r) *np.sin(theta_goal))
        else:
          delx[i][j]  = (50 * (d_goal-r) *np.cos(theta_goal))
          dely[i][j]  = (50 * (d_goal-r) *np.sin(theta_goal))
        
      if d_goal>r+s:
        if delx[i][j] != 0:
          delx[i][j] += 50* s *np.cos(theta_goal)
          dely[i][j] += 50* s *np.sin(theta_goal)
        else:
          delx[i][j] = 50* s *np.cos(theta_goal)
          dely[i][j] = 50* s *np.sin(theta_goal)

  fig, ax = plt.subplots(figsize=(10, 10))
  ax.quiver(X, Y, delx, dely)

  #obstacle
  ax.add_patch(plt.Circle(obstacle, r, color='y'))
  ax.annotate("Obstacle", xy=obstacle, fontsize=8, ha="center")

  #goal
  ax.add_patch(plt.Circle(goal, r, color='m'))
  ax.annotate("Goal", xy=goal, fontsize=10, ha="center")

  #drone
  ax.add_patch(plt.Circle(drone, r, color='r'))
  ax.annotate("Drone", xy=drone, fontsize=7, ha="center")

  fig.canvas.draw()
  fig.canvas.flush_events()

# distance
def distance(x, y):
  dist = np.linalg.norm(x - y)
  return dist

def c(d, g):
  ret = np.power(d-g, 2)
  return ret

# movimento a caso
while distance(drone, goal) > epsilon:
  # 1. compute the gradient decent of the cost function
  # 2. take the oppotite direction
  # 3. compute the time step
  # 4. update drone position

  # IO
  draw()

  # input to slow execution
  a = input()

  # close to prevent opening
  plt.close()
  