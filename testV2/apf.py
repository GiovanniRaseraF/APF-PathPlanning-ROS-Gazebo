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
    def __init__(self, x: float, y: float):
        print(f"Obstacle2D({x}, {y})")
        self.x = np.array(x)
        self.y = np.array(y)

class Goal2D():
    def __init__(self, x: float, y: float):
        print(f"Goal2D({x}, {y})")
        self.x = np.array(x)
        self.y = np.array(y)

class APF2D():
    def __init__(self, s_ize: int = DEFAULT_DIM_SIZE):
        print(f"APF2D([{s_ize}][{s_ize}])")
        self.obstacle: Obstacle2D | None = None
        self.goal: Goal2D | None = None
        self.s_ize = s_ize
        self.a = [i + 0.5 for i in range(s_ize)]
        self.b = [i + 0.5 for i in range(s_ize)]
        self.p0 = [(x, y) for x in self.a for y in self.b]
        self.p1 = (-7.9, 0.4)
        self.p2 = (4.8, 0.56)
        self.v1 = [(xp1 - self.p1[0], yp1 - self.p1[1]) for (xp1, yp1) in self.p0]
        self.v2 = [(-(xp2 - self.p2[0]), -(yp2 - self.p2[1])) for (xp2, yp2) in self.p0]

    # TODO: ragi this needs to update the field ???
    # need to decide if this is a good idea
    def update_goal(self, new_goal : Goal2D) -> int:
        self.goal = new_goal
        return 0
    
    def update_obstacle(self, new_obstacle: Obstacle2D) -> int:
        self.obstacle = new_obstacle
        return 0

    def calculate(self) -> None:
        for i in range(self.s_ize):
            for j in range(self.s_ize):
                pass