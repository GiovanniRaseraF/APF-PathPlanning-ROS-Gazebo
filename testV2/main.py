"""
Title: Calculate APF
Author: Giovanni Rasera
"""

from apf import *
from viz import *
import time

def main(gridSize=20):
    goal = Goal2D(gridSize/2, gridSize/2, 1)
    # obs1 = Obstacle2D(0, 0, 1)
    field = APF2D(gridSize)

    # Add data
    field.update_goal(goal)
    # field.insert_obstacle(obs1)

    # Calculate APF
    field.calculate()

    # Draw
    vis, data3d = draw(field)
    vis.create_window(width=1000, height=1000)

    for x in range(gridSize):
        for y in range(gridSize):
            # field.obstacles[0].x = x
            # field.obstacles[0].y = y
            field.goal.x = x
            field.goal.y = y
            field.calculate()
            vis, data3d = draw(field)
            vis.create_window(width=1000, height=1000)

            for m in data3d:
                vis.add_geometry(m)
            vis.poll_events()
            vis.update_renderer()

            time.sleep(0.5)
            vis.destroy_window()
    
    # Exit
    input("Enter to exit...")

if __name__ == "__main__":
    main()