"""
Title: Calculate APF
Author: Giovanni Rasera
"""

import numpy as np
import time
import math

DEFAULT_DIM_SIZE: int = 100

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
        self.obstacles: list(Obstacle2D) = []
        self.goal: Goal2D | None = None
        self.gridSize = gridSize
        self.x = np.arange(self.gridSize)
        self.y = np.arange(self.gridSize)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.delx = np.zeros_like(self.X)
        self.dely = np.zeros_like(self.Y)

    def update_goal(self, new_goal : Goal2D) -> None:
        self.goal = new_goal

    def calculate(self) -> None:
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                # finding the goal distance and obstacle distance
                if self.goal is not None:
                    d_goal = np.sqrt((self.goal.x - self.X[i][j])**2 + ((self.goal.y - self.Y[i][j]))**2)
                # d_obstacle = np.sqrt((obstacle[0]-X[i][j])**2 + (obstacle[1]-Y[i][j])**2)

                #finding theta correspoding to the goal and obstacle 
                    theta_goal = np.arctan2(self.goal.y - self.Y[i][j], self.goal.x  - self.X[i][j])
                # theta_obstacle = np.arctan2(obstacle[1] - Y[i][j], obstacle[0]  - X[i][j])
        
                # if (flag_Obstacle):
                #     if d_obstacle < r:
                #         delx[i][j] += 0
                #         dely[i][j] += 0
                #     elif (d_obstacle>=r and d_obstacle<r+s) :
                #         delx[i][j] += -β * (s+r-d_obstacle) * np.cos(theta_obstacle)
                #         dely[i][j] += -β * (s+r-d_obstacle) * np.sin(theta_obstacle) 
                #     elif d_obstacle>=r+s:
                #         delx[i][j] += 0 
                #         dely[i][j] += 0 
      
                # if (flag_Goal):    
                #     if d_goal <r+s:
                #         delx[i][j] += (50 * (d_goal-r) * np.cos(theta_goal))
                #         dely[i][j] += (50 * (d_goal-r) * np.sin(theta_goal))
                #     if d_goal>=r+s:
                #         delx[i][j] += 50 * s * np.cos(theta_goal)
                #         dely[i][j] += 50 * s * np.sin(theta_goal)