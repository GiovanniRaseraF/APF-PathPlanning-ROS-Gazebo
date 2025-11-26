"""
Title: Calculate APF
Author: Giovanni Rasera
"""

import numpy as np
import open3d as o3d
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

def draw(field: APF2D) -> None:
    # Build scene
    grid = create_grid(field.gridSize)
    first_point = create_ball([0, 0, 0], radius=0.01)
    last_point = create_ball([int(field.gridSize), int(field.gridSize), 0], radius=0.01)

    # Goal
    goal_point = first_point
    if field.goal:
        goal_point = create_ball([int(field.goal.x), int(field.goal.y), 0], radius=field.goal.r, color=[0, 1, 0])
    
    # obstacles
    obstacles_points = []
    for obs in field.obstacles:
        obs_point = create_ball([int(obs.x), int(obs.y), 0], radius=obs.r, color=[1, 0, 0])
        obstacles_points.append(obs_point)

    # Viz
    o3d.visualization.draw_geometries([grid, goal_point, *obstacles_points, first_point, last_point])