from apf import *

def main():
    goal = Goal2D(100, 100, 1)
    obs1 = Obstacle2D(0, 0, 1)
    field = APF2D()

    field.calculate()
    field.update_goal(goal)
    field.calculate()

if __name__ == "__main__":
    main()