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

def get_arrow(origin, vector, color=[0, 0, 1], scale=1.0):
    """
    Creates an arrow geometry located at 'origin' pointing in 'vector' direction.
    """
    arrow = o3d.geometry.TriangleMesh.create_arrow(
        cylinder_radius=0.01 * scale,
        cylinder_height=0.1 * scale,
        cone_radius=0.04 * scale,
        cone_height=0.04 * scale
    )
    
    # Rotate 
    R_y = arrow.get_rotation_matrix_from_xyz((0, np.pi / 2, 0))
    arrow.rotate(R_y, center=(0, 0, 0))
    
    angle = np.arctan2(vector[1], vector[0])
    R_z = arrow.get_rotation_matrix_from_xyz((0, 0, angle))
    arrow.rotate(R_z, center=(0, 0, 0))

    # Translate to position
    arrow.translate(origin)

    # Color
    arrow.paint_uniform_color(color)
    
    return arrow

def create_vector_field(field):
    """
    Generates a single mesh containing arrows for the entire grid.
    """
    combined_mesh = o3d.geometry.TriangleMesh()
    
    for x in range(0, int(field.gridSize)):
        for y in range(0, int(field.gridSize)):
            pos = np.array([x, y])

            # TODO: ragi add vector field creation
            arrow = get_arrow(origin=[x+0.5, y+0.5, 0], vector=[field.delx[x][y], field.dely[x][y]], scale=3.0)
            combined_mesh += arrow

    return combined_mesh

def draw(field: APF2D):
    # Build scene
    grid = create_grid(field.gridSize)
    first_point = create_ball([0, 0, 0], radius=0.1)
    last_point = create_ball([int(field.gridSize), int(field.gridSize), 0], radius=0.1)

    # Goal
    goal_point = first_point
    if field.goal:
        goal_point = create_ball([int(field.goal.x), int(field.goal.y), 0], radius=field.goal.r, color=[0, 1, 0])
    
    # Obstacles
    obstacles_points = []
    for obs in field.obstacles:
        obs_point = create_ball([int(obs.x), int(obs.y), 0], radius=obs.r, color=[1, 0, 0])
        obstacles_points.append(obs_point)

    # Field Speeds
    vector_field = create_vector_field(field)

    vis = o3d.visualization.Visualizer()
    data3d = [grid, goal_point, *obstacles_points, first_point, last_point, vector_field]

    return vis, data3d