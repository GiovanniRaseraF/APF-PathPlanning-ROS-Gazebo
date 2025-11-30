"""
Title: Calculate APF
Author: Giovanni Rasera
"""

from apf import *
from viz import *

def move_up(vis, field):
    print("Down Arrow Pressed")
    field.obstacles[0].y += 1
    field.calculate()
    return False

def move_down(vis, field):
    print("Down Arrow Pressed")
    field.obstacles[0].y -= 1
    field.calculate()
    return False

def main(gridSize=20):
    goal = Goal2D(gridSize, gridSize, 1)
    obs1 = Obstacle2D(gridSize/2, gridSize/2, 1)
    field = APF2D(gridSize)

    # Add data
    field.update_goal(goal)
    field.insert_obstacle(obs1)

    # Calculate APF
    field.calculate()

    # Draw
    vis, data3d = draw(field)
    vis.create_window(width=800, height=800)

    # TODO: ragi this does not exits, find a solution to listen to key callbacks
    # vis.register_key_callback(ord("w"), move_up, field)
    # vis.register_key_callback(ord("s"), move_down, field)
    # vis.register_key_callback(ord("q"), exit)

    for m in data3d:
        vis.add_geometry(m)
    vis.poll_events()
    vis.update_renderer()
    
    # Exit
    input("Enter to exit...")
    vis.destroy_window()

if __name__ == "__main__":
    main()