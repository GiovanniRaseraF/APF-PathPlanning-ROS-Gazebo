"""
Title: Calculate APF
Author: Giovanni Rasera
"""

import numpy as np
import open3d as o3d
import copy
from apf import *

def create_grid(size=100, step=1):
    """
    Create a square grid of given size on the XY plane.
    Lines run from (0,0) to (size,size).
    """
    lines = []
    points = []

    # Vertical lines
    for x in range(0, size + 1, step):
        points.append([x, 0, 0])
        points.append([x, size, 0])
        lines.append([len(points)-2, len(points)-1])

    # Horizontal lines
    for y in range(0, size + 1, step):
        points.append([0, y, 0])
        points.append([size, y, 0])
        lines.append([len(points)-2, len(points)-1])

    line_set = o3d.geometry.LineSet(
        points=o3d.utility.Vector3dVector(np.array(points)),
        lines=o3d.utility.Vector2iVector(np.array(lines))
    )

    # Optional: color the grid grey
    colors = [[0.7, 0.7, 0.7] for _ in lines]
    line_set.colors = o3d.utility.Vector3dVector(colors)

    return line_set

def create_ball(position, radius=1.0, color=[1, 0, 0]):
    """
    Creates a sphere (ball) at a given 3D position.
    """
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=radius)
    sphere.compute_vertex_normals()
    sphere.paint_uniform_color(color)
    sphere.translate(position)

    return sphere

def create_from_array(arr, radius=0.05, color=[0, 0, 0]):
    balls = []
    for p in arr:
        ball = create_ball([p[0], p[1], 0], radius=radius, color=color)
        balls.append(ball)
    return balls

def draw(field: APF2D):
    # Build scene
    grid = create_grid(field.s_ize*2, step=1)
    first_point = create_ball([0, 0, 0], radius=0.05)
    last_point = create_ball([field.s_ize, field.s_ize, 0], radius=0.05, color=[1, 0, 0])

    # # Goal
    goal_point = create_ball([field.goal[0], field.goal[1], 0], radius=0.05, color=[0, 1, 0])
    obstacle_point = create_ball([field.obstacle[0], field.obstacle[1], 0], radius=0.05, color=[1, 0, 0])

    points_p0 = create_from_array(field.halfPoints)
    points_v3 = create_from_array(field.v3, radius=0.02, color=[0, 1, 1])
    # # Obstacles
    # obstacles_points = []
    # for obs in field.obstacles:
    #     obs_point = create_ball([int(obs.x), int(obs.y), 0], radius=obs.r, color=[1, 0, 0])
    #     obstacles_points.append(obs_point)

    # # Field Speeds
    # vector_field = create_vector_field(field)

    vis = o3d.visualization.Visualizer()
    data3d = [grid, *points_p0, *points_v3, goal_point, obstacle_point, first_point, last_point]

    return vis, data3d