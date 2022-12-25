import math
from pystdlib import stddraw as sd

print("spirographs")

R, r, a = map(float, input().split())


print("R=", R, "r=", r, "a=", a)

DIM = 30

IMAGE_SIZE = 1024

sd.setCanvasSize(IMAGE_SIZE, IMAGE_SIZE)

sd.setXscale(-DIM, DIM)
sd.setYscale(-DIM, DIM)

sd.clear(sd.CYAN)


def fx(angle):
    return (R + r) * math.cos(angle) - (r + a) * math.cos((R + r) * angle / r)


def fy(angle):
    return (R + r) * math.sin(angle) - (r + a) * math.sin((R + r) * angle / r)


x = [fx(0)]
y = [fy(0)]

POINTS = 100000

delta_alpha = 200 * math.pi / POINTS

for i in range(1, POINTS + 1):
    angle = i * delta_alpha
    x.append(fx(angle))
    y.append(fy(angle))

    sd.line(x[i - 1], y[i - 1], x[i], y[i])


sd.show()
