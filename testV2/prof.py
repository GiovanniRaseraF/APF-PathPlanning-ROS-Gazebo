import cProfile
import argparse

from apf import *

def main(profiler: cProfile.Profile):
    goal = Goal2D(100, 100, 1)
    obs1 = Obstacle2D(0, 0, 1)
    field = APF2D()
    field.update_goal(goal)
    ret = field.insert_obstacle(obs1)

    # Profile algo
    profiler.enable()
    field.calculate()
    profiler.disable()

    # Save and run 
    # snakeviz field_calculate.prof

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Profiling APF')
    parser.add_argument('filename', help='file to dump profiling')
    args = parser.parse_args()
    
    profiler = cProfile.Profile()
    main(profiler)
    profiler.dump_stats(args.filename)