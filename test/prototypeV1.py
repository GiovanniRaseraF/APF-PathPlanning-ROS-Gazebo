#
# Authors: 
#   - Giovanni Rasera
#   - Diletta Giabardo
#

import numpy as np
import matplotlib.pyplot as plt
import time
import math

# initial input
dx = int(input("DroneX: "))
dy = int(input("DroneY: "))

ox = int(input("ObstX: "))
oy = int(input("ObstY: "))

gx = int(input("GoalX: "))
gy = int(input("GoalY: "))

#drone
drone = np.array([dx, dy])
goal = np.array([gx, gy])
obstacle = np.array([ox, oy])

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

# plotting
plt.ion()

def calcForceField():
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

def draw():
  fig, ax = plt.subplots(figsize=(10, 10))
  ax.quiver(X, Y, delx, dely)

  # obstacle
  if(flag_Obstacle):  
    ax.add_patch(plt.Circle(obstacle, r, color='y'))
    ax.annotate("Obstacle", xy=obstacle, fontsize=8, ha="center")

  # goal
  if(flag_Goal):
    ax.add_patch(plt.Circle(goal, r, color='m'))
    ax.annotate("Goal", xy=goal, fontsize=8, ha="center")

  # drone
  ax.add_patch(plt.Circle(drone, r, color='r'))
  ax.annotate("Drone", xy=drone, fontsize=1, ha="center")

  # history path
  ax.plot(dronePosesX, dronePosesY, label="poses", linestyle="-")

  fig.canvas.draw()
  fig.canvas.flush_events()

# distance
def distance(x, y):
  dist = np.linalg.norm(x - y)
  return dist

def c(d, g):
  ret = np.power(d-g, 2)
  return ret

# create force field
calcForceField()

maxForseX = delx.max()
maxForseY = dely.max()

# counter
counter = 0

# movimento a caso
while distance(drone, goal) > epsilon:
  # store position
  dronePosesX.append(drone[0])
  dronePosesY.append(drone[1])

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
    delx[droneGridPos[1]][droneGridPos[0]], 
    dely[droneGridPos[1]][droneGridPos[0]]
  ])

  # calculate force to apply
  realForceOnDrone = (np.array([
    forceOnDrone[0] / maxForseX,
    forceOnDrone[1] / maxForseY
  ]))

  print(f"droneGridPos: {droneGridPos}")
  print(f"forceOnDrone: {forceOnDrone}")
  print(f"realForceOnDrone: {realForceOnDrone}")

  # move the drone 
  drone = drone + realForceOnDrone

  # when to end
  if(drone[0]>= 50 or drone[1] >= 50):
    break

  if(counter % 60 == 0):
    draw()
    i = input()
    plt.close()

  counter+=1

  print(f"dronePos: {drone}")
  # 3. compute the time step
  # 4. update drone position

# IO
draw()

# input to slow execution
a = input("Exit> ")

# close to prevent opening
plt.close()
  