"""
Title: Calculate APF
Author: Giovanni Rasera
"""

from apf import *
from viz import *

def main():
    gridSize = 20
    goal = Goal2D(gridSize-1, gridSize-1, 1)
    obs1 = Obstacle2D(gridSize/2, gridSize/2, 1)
    field = APF2D(gridSize)

    field.update_goal(goal)
    field.insert_obstacle(obs1)

    field.calculate()
    draw(field)

if __name__ == "__main__":
    main()