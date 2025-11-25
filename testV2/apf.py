"""
Title: Calculate APF
Author: Giovanni Rasera
"""

import numpy as np

DEFAULT_DIM_SIZE: int = 100

# TODO: ragi control parameters
α = 50
β = 140
s = 8

class Obstacle2D():
    def __init__(self, x: float, y: float, r: float):
        print(f"Obstacle2D({x}, {y}, {r})")
        self.x = np.array([x])
        self.y = np.array([y])
        self.r = np.array([r])

class Goal2D():
    def __init__(self, x: float, y: float, r: float):
        print(f"Goal2D({x}, {y}, {r})")
        self.x = np.array([x])
        self.y = np.array([y])
        self.r = np.array([r])

class APF2D():
    def __init__(self, gridSize: int = DEFAULT_DIM_SIZE):
        print(f"APF2D([{gridSize}][{gridSize}])")
        self.obstacles: list[Obstacle2D] = []
        self.goal: Goal2D | None = None
        self.gridSize = gridSize
        self.x = np.arange(self.gridSize)
        self.y = np.arange(self.gridSize)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.delx = np.zeros_like(self.X)
        self.dely = np.zeros_like(self.Y)

    def update_goal(self, new_goal : Goal2D) -> None:
        self.goal = new_goal
    
    def insert_obstacle(self, new_obstacle: Obstacle2D) -> int:
        self.obstacles.append(new_obstacle)

        # TODO: this should be the id of the obstacle to be able to delete it
        return 0

    def calculate(self) -> None:
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                # Compute the goal
                if self.goal is not None:
                    d_goal = np.sqrt((self.goal.x - self.X[i][j])**2 + ((self.goal.y - self.Y[i][j]))**2)
                    theta_goal = np.arctan2(self.goal.y - self.Y[i][j], self.goal.x  - self.X[i][j])

                    if d_goal < self.goal.r+s:
                        self.delx[i][j] += (50 * (d_goal - self.goal.r) * np.cos(theta_goal))
                        self.dely[i][j] += (50 * (d_goal - self.goal.r) * np.sin(theta_goal))
                    if d_goal >= self.goal.r+s:
                        self.delx[i][j] += 50 * s * np.cos(theta_goal)
                        self.dely[i][j] += 50 * s * np.sin(theta_goal)

                # Compute one obstacle
                # TODO: ragi add full obstacles control
                if len(self.obstacles) > 0:
                    d_obstacle = np.sqrt((self.obstacles[0].x - self.X[i][j])**2 + (self.obstacles[0].y - self.Y[i][j])**2)
                    theta_obstacle = np.arctan2(self.obstacles[0].y - self.Y[i][j], self.obstacles[0].x - self.X[i][j])
        
                    if (d_obstacle >= self.obstacles[0].r and d_obstacle<self.obstacles[0].r + s) :
                        self.delx[i][j] += -β * (s + self.obstacles[0].r - d_obstacle) * np.cos(theta_obstacle)
                        self.dely[i][j] += -β * (s + self.obstacles[0].r - d_obstacle) * np.sin(theta_obstacle) 
                    else:
                        self.delx[i][j] = 0
                        self.dely[i][j] = 0
      
                    