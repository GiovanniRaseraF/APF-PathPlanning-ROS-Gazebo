import cProfile
from apf import *

def main():
    goal = Goal2D(100, 100, 1)
    obs1 = Obstacle2D(0, 0, 1)
    field = APF2D()
    field.update_goal(goal)
    ret = field.insert_obstacle(obs1)

    # Profile algo
    profiler = cProfile.Profile()
    profiler.enable()

    field.calculate()

    profiler.disable()
    profiler.dump_stats("example.prof")

if __name__ == "__main__":
    main()