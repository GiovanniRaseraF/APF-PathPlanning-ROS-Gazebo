"""
Title: Calculate APF
Author: Giovanni Rasera
"""

from apf import *
from viz import *
import time

def main(gridSize=10):
    field = APF2D(gridSize)

    # vis, data3d = draw(field)
    # vis.create_window(width=1000, height=1000)
    # for m in data3d:
    #     vis.add_geometry(m)
    # vis.poll_events()
    # vis.update_renderer()
    
    # Exit
    # input("Enter to exit...")
    # vis.destroy_window()

if __name__ == "__main__":
    main(10)