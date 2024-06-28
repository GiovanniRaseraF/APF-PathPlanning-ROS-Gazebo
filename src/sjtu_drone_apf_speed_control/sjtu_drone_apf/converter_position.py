import math as Math

# Author: Diletta Giabardo

#gazebo world
gmaxx = 0
gmaxy = 20
gminx = 20
gminy = 0

#python world
pmaxx = 50
pmaxy = 50
pminx = 0
pminy = 0

# allow to change boundares for waypointing
def newBoundaries(newgmaxx, newgminx, newgmaxy, newgminy):
    global gmaxx
    global gminx
    global gmaxy
    global gminy
    gmaxx = newgmaxx
    gminx = newgminx
    gmaxy = newgmaxy
    gminy = newgminy

# convert from gazebo coordinates to matrix
def gazebo_to_python(gx, gy): 
    # x
    abs_distance_x = abs(gmaxx - gminx)
    abs_distance_drone_x = abs_distance_x - abs(gmaxx - gx)
    div_len_x = abs_distance_x / pmaxx
    px = Math.floor(abs_distance_drone_x / div_len_x)

    print(f"abs_distance_x:{abs_distance_x}")
    print(f"abs_distance_drone_x:{abs_distance_drone_x}")
    print(f"div_len_x:{div_len_x}")
    print(f"px:{px}")

    # y
    abs_distance_y = abs(gmaxy - gminy)
    abs_distance_drone_y = abs_distance_y - abs(gmaxy - gy)
    div_len_y = abs_distance_y / pmaxy
    py = Math.floor(abs_distance_drone_y / div_len_y) 

    print(f"abs_distance_y:{abs_distance_y}")
    print(f"abs_distance_drone_y:{abs_distance_drone_y}")
    print(f"div_len_y:{div_len_y}")
    print(f"px:{py}")

    return px, py

def python_to_gazebo(px, py):
    
    gx = Math.floor(((px - pminx) * (gmaxx - gminx) / (pmaxx - pminx)) + gminx)
    gy = Math.floor(((py - pminy) * (gmaxy - gminy) / (pmaxy - pminy)) + gminy)

    return gx, gy
