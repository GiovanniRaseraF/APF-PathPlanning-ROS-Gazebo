from apf import *
from viz import *

# plotting
plt.ion()

def main():
    goal = Goal2D(9, 9, 1)
    obs1 = Obstacle2D(5, 5, 1)
    field = APF2D(10)

    field.update_goal(goal)
    field.insert_obstacle(obs1)

    field.calculate()

    draw(field)

    input("Enter to close >>>")

    plt.close()

if __name__ == "__main__":
    main()