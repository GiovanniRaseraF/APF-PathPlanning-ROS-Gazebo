import numpy as np
import matplotlib.pyplot as plt
import time

#drone
drone = [10, 10]

s = 15
r=2
"""
    Inside the nested loop, distance from each point to the goal and ostacle is 
    calculated, Similarly angles are calculated. 
    α = 50
    β = 50
    s = 15
    r = 2
"""

plt.ion()
figure = plt.figure()

def draw():
  x = np.arange(-0,50,1)
  y = np.arange(-0,50,1)

  # Goal is at (40,40) 
  goal = [40,40]

  #obstacle is at(25,25)
  obstacle = [20, 20]

  X, Y = np.meshgrid(x,y)

  delx = np.zeros_like(X)
  dely = np.zeros_like(Y)

  # creazione del potential field
  for i in range(len(x)):
    for j in range(len(y)):
    
      # finding the goal distance and obstacle distance
      d_goal = np.sqrt((goal[0]-X[i][j])**2 + ((goal[1]-Y[i][j]))**2)
      d_obstacle = np.sqrt((obstacle[0]-X[i][j])**2 + (obstacle[1]-Y[i][j])**2)
      #print(f"{i} and {j}")

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

  ax.set_title('Combined Potential when Goal and Obstacle are different ')

  for i in zip(delx, dely):
    print(i)

#####################qui di seguito: ROBOT motion nel PF ##############################
## creare una funzione di espone per vettori
# def c(drone, goal):
#   return np.pow(drone-goal, 2)

# epsilon = 1
# while || drone - goal || > epsilon:
#   # compute gradient of the cost function  
#   cdrone = c(drone, goal)
#   DerivXcdrone = PDerive(cdrone, "x")
#   DerivYcdrone = PDerive(cdrone, "y")
#   DeltaCdrone = Traspose(DerivXcdrone, DerivXcdrone)

#   # take the opposite direction
#   Ddrone = - DeltaCdrone / || DeltaCdrone ||

#   # compute the time step
#   Tstardrone = argmin(Tdrone, c(drone + Tdrone*Ddrone, goal))

#   # update posizion
# movimento a caso
for i in range(0, 30):
  drone = (i, i)
  draw()
  figure.canvas.draw()
  figure.canvas.flush_events()
  time.sleep(1)