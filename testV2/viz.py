import matplotlib.pyplot as plt
import numpy as np
import math
from apf import *

def draw(field: APF2D) -> None:
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.quiver(field.X, field.Y, field.delx, field.dely)

    # goal
    if field.goal:
        goal_xy = [field.goal.x, field.goal.y]
        ax.add_patch(plt.Circle(goal_xy, min(1, int(field.goal.r)), color='g'))
        ax.annotate("Goal", xy=goal_xy, fontsize=4, ha="center")

    # obstacles
    for obs in field.obstacles:
        obs_xy = [obs.x, obs.y]
        ax.add_patch(plt.Circle(obs_xy, min(1, int(obs.r)), color='r'))
        ax.annotate("O", xy=obs_xy, fontsize=4, ha="center")

    # drone
    # ax.add_patch(plt.Circle(drone, r, color='r'))
    # ax.annotate("Drone", xy=drone, fontsize=1, ha="center")

    # history path
    # ax.plot(dronePosesX, dronePosesY, label="poses", linestyle="-")

    fig.canvas.draw()
    fig.canvas.flush_events()