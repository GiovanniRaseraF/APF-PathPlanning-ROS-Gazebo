"""
Title: Calculate APF
Author: Giovanni Rasera
"""

import cProfile
import argparse

from apf import *

def run(profiler: cProfile.Profile, gridSize: int):
    goal = Goal2D(100, 100, 1)
    obs1 = Obstacle2D(0, 0, 1)
    field = APF2D(gridSize)
    field.update_goal(goal)
    ret = field.insert_obstacle(obs1)

    # Profile algo
    profiler.enable()
    field.calculate()
    profiler.disable()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Profiling APF2D')
    parser.add_argument('filename', help='filename to dump profiling')
    parser.add_argument('size', help='size of the APF grid', type=int, default=DEFAULT_DIM_SIZE)
    args = parser.parse_args()
    
    profiler = cProfile.Profile()

    run(profiler, args.size)

    profiler.dump_stats(f"{args.size}_{args.filename}")