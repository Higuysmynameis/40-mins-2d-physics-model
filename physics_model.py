import math
import matplotlib.pyplot as plt
import time

print("Physics Model")


def proj_motion():
    v0 = float(input("velocity"))
    angle = int(input("angle"))
    h0 = float(input("height"))
    g = 9.81
    t = (2 * v0 * math.sin(angle)) / g
    x = v0 * math.cos(angle) * t

    y = h0 + (v0 * math.sin(angle) * t) - (0.5 * g * t ** 2)

    print("Time of flight: ", t)
    print("Maximum horizontal distance: ", x)
    print("Maximum vertical distance: ", y)
    print("====Graphing===>")

    x_vals = [v0 * math.cos(math.radians(angle)) * t
              for t in range(int(t * 10))]
    y_vals = [h0 + (v0 * math.sin(math.radians(angle)) * t) - (0.5 * g * t ** 2)
              for t in range(int(t * 10))]
    f, ax = plt.subplots()
    ax.plot(x_vals, y_vals)
    ax.set(xlabel='horizontal distance (m)', ylabel='vertical distance (m)',
           title='Projectile Motion')

    time.sleep(4)
    plt.show()


proj_motion()