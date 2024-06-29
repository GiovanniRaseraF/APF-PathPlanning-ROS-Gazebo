
#
# Authors: 
#   - Giovanni Rasera
#   - Diletta Giabardo
#

import numpy as np
import time
import math

#drone
drone = np.array([25, 0])
goal = np.array([25, 50])
obstacle = np.array([25, 10])

# history
dronePosesX = []
dronePosesY = []

# intensity modeling
flag_Goal = True
flag_Obstacle = True
α = 50 #
β = 140
s = 8
r = 2

# epsilon
epsilon = 1

# gridSize
gridSize = 100

# field
x = np.arange(-0,gridSize,1)
y = np.arange(-0,gridSize,1)
X, Y = np.meshgrid(x,y)
delx = np.zeros_like(X)
dely = np.zeros_like(Y)

REP_FORCE = 300

def setNewPositioning(newgoal : np.array, newobstacle : np.array):
  global drone
  global goal
  global obstacle

  global dronePosesX
  global dronePosesY

  global flag_Goal
  global flag_Obstacle

  global x
  global y
  global X, Y
  global delx
  global dely
  
  goal = newgoal
  obstacle = newobstacle

  calcForceField()

def calcForceField():
  global drone
  global goal
  global obstacle

  global dronePosesX
  global dronePosesY

  global flag_Goal
  global flag_Obstacle

  global x
  global y
  global X, Y
  global delx
  global dely

  for i in range(len(x)):
    for j in range(len(y)):
      
      # finding the goal distance and obstacle distance
      d_goal = np.sqrt((goal[0]-X[i][j])**2 + ((goal[1]-Y[i][j]))**2)
      d_obstacle = np.sqrt((obstacle[0]-X[i][j])**2 + (obstacle[1]-Y[i][j])**2)

      #finding theta correspoding to the goal and obstacle 
      theta_goal= np.arctan2(goal[1] - Y[i][j], goal[0]  - X[i][j])
      theta_obstacle = np.arctan2(obstacle[1] - Y[i][j], obstacle[0]  - X[i][j])
        
      if (flag_Obstacle):
        if d_obstacle < r:
          delx[i][j] +=0
          dely[i][j] +=0
        elif (d_obstacle>=r and d_obstacle<r+s) :
          delx[i][j] += -β *(s+r-d_obstacle)* np.cos(theta_obstacle)
          dely[i][j] += -β * (s+r-d_obstacle)* np.sin(theta_obstacle) 
        elif d_obstacle>=r+s:
          delx[i][j] +=0 
          dely[i][j] +=0 
      
      if (flag_Goal):    
        if d_goal <r+s:
          delx[i][j]  += (50 * (d_goal-r) *np.cos(theta_goal))
          dely[i][j]  += (50 * (d_goal-r) *np.sin(theta_goal))
        if d_goal>=r+s:
          delx[i][j] += 50* s *np.cos(theta_goal)
          dely[i][j] += 50* s *np.sin(theta_goal)


def get_field_power(x: int, y: int, scale_x: float, scale_y: float):
  global drone
  global goal
  global obstacle

  global dronePosesX
  global dronePosesY

  global flag_Goal
  global flag_Obstacle

  global X, Y
  global delx
  global dely

  # scaling
  minForseX = delx.min()
  maxForseX = delx.max()
  minForseY = dely.min()
  maxForseY = dely.max()

  dstX = abs(maxForseX) + abs(minForseX)
  dstY = abs(maxForseY) + abs(minForseY)

  print(f"maxforceX {maxForseX}")

  if(x < 0): x = 0
  if(x > (gridSize-1)): x = (gridSize-1)
  if(y < 0): y = 0
  if(y > (gridSize-1)): y = (gridSize-1)

  # positioning
  forceOnDrone = np.array([
    delx[x][y], 
    dely[x][y]
  ])

  # calculate force to apply
  realForceOnDrone = (np.array([
    (forceOnDrone[0] / dstX) * 2,
    (forceOnDrone[1] / dstY) * 2,
  ]))

  # actual speed
  ret_x_speed = realForceOnDrone[0]
  ret_y_speed = realForceOnDrone[1]

  return ret_x_speed, ret_y_speed