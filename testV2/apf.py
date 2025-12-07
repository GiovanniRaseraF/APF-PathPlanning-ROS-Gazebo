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

def calc_field(p0: np.array, v_1: np.array, v_2: np.array, c: float = 57.0, t: float = 1) -> np.array:
    v1_m = np.array([0, 0])
    v2_m = np.array([0, 0])
    v1possible = False
    v2possible = False
    if (v_1[0] != 0 or v_1[1] != 0):
        v1_m = v_1 / ((v_1[0] ** 2 + v_1[1] ** 2)**(1/2))
        v1possible = True

    if (v_2[0] != 0 or v_2[1] != 0):
        v2_m = v_2 / ((v_2[0] ** 2 + v_2[1] ** 2)**(1/2))
        v2possible = True

    if(v1possible and v2possible):
        v1_n = 1 / (np.dot(v_1, v_1) + c) * t
        v2_n = 1 / (np.dot(v_2, v_2) + c) * t
        v_3 = p0 + (c + 1) * (v1_m * v1_n + v2_m * v2_n)
        return v_3
    else:
        return p0

class APF2D():
    

    def __init__(self, s_ize: int = DEFAULT_DIM_SIZE):
        print(f"APF2D([{s_ize}][{s_ize}])")
        self.s_ize = s_ize
        self.a = np.array([i+0.5 for i in range(0, s_ize+1)])
        self.b = np.array([i+0.5 for i in range(0, s_ize+1)])
        self.halfPoints = np.array([(y, x) for x in self.a for y in self.b])
        # goal
        self.goal = np.array([5, 0])
        # obstacle
        self.obstacle = np.array([5, 10])
        self.v1 = np.array([(xp1 - self.goal[0], yp1 - self.goal[1]) for (xp1, yp1) in self.halfPoints])
        self.v2 = np.array([(-(xp2 - self.obstacle[0]), -(yp2 - self.obstacle[1])) for (xp2, yp2) in self.halfPoints])

        self.c = 100.0
        self.t = 0.5
        self.calculate()

    # TODO: ragi this needs to update the field ???
    def update_goal(self, new_goal : np.array) -> int:
        self.goal = new_goal
        return 0
    
    def update_obstacle(self, new_obstacle: np.array) -> int:
        self.obstacle = new_obstacle
        return 0

    def calculate(self) -> None:
        self.v3 = np.array([calc_field(p, v1, v2, self.c, self.t) for p, v1, v2 in zip(self.halfPoints, self.v1, self.v2)])