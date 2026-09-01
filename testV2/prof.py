"""
Title: Calculate APF
Author: Giovanni Rasera
"""

import cProfile
import argparse
from main import main
from apf import *

def run(profiler: cProfile.Profile, gridSize: int):
    # Profile algo
    profiler.enable()
    main(gridSize=gridSize)
    profiler.disable()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Profiling APF2D')
    parser.add_argument('filename', help='filename to dump profiling')
    parser.add_argument('size', help='size of the APF grid', type=int, default=DEFAULT_DIM_SIZE)
    args = parser.parse_args()
    
    profiler = cProfile.Profile()

    run(profiler, args.size)

    profiler.dump_stats(f"{args.size}_{args.filename}")