import math as Math

# Author: Diletta Giabardo

#gazebo world
gmaxx = 9.42472
gmaxy = 9.27499
gminx = -9.26194
gminy = -9.39923
#python world
pmaxx = 50
pmaxy = 50
pminx = 0
pminy = 0

def gazebo_to_python(gx, gy): 
    # x
    abs_distance_x = abs(gmaxx) - abs(gminx)
    abs_distance_drone_x = abs_distance_x - (abs(gmaxx) - abs(gx))
    div_len_x = abs_distance_x / pmaxx
    px = Math.floor(abs_distance_drone_x / div_len_x)

    # y
    abs_distance_y = abs(gmaxy) - abs(gminy)
    abs_distance_drone_y = abs_distance_y - (abs(gmaxy) - abs(gy))
    div_len_y = abs_distance_y / pmaxy
    py = Math.floor(abs_distance_drone_y / div_len_y) 

    return px, py

def python_to_gazebo(px, py):
    
    gx = Math.floor(((px - pminx) * (gmaxx - gminx) / (pmaxx - pminx)) + gminx)
    gy = Math.floor(((py - pminy) * (gmaxy - gminy) / (pmaxy - pminy)) + gminy)

    return gx, gy
