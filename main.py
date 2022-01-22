import matplotlib
from constants import *
from vector import *
from particle import *
from matplotlib import pyplot as plt
from math import degrees, radians, atan
import numpy as np

def coulombs(esu: float) -> float:
    '''Convert electrostatic charge units to Coulombs'''
    return esu * (3.335640951982E-10)

def F(Q1: float, Q2: float, r: float) -> float:
    '''Apply Coulomb's law to get the force between two particles

    Charges should be in ESU'''

    # Apply Coulomb's law - this calculates the force based on the ESU charges
    # It's better to do this *before* converting as large integers in Python have unlimited
    # width whereas small decimals are limited-precision.
    out = (1 / (4 * pi * ε0)) * ((Q1 * Q2) / r ** 2)

    return coulombs(coulombs(out))

def main():
    particles = {d : Particle(V2(-20, d), V2(1, 0)) for d in np.arange(-2, 2, 0.004)}
    goldPos = V2(0, 0)
    for particle in particles.values():
        f = F(2, 79, particle.pos.dst(goldPos))
        while F(2, 79, particle.pos.dst(goldPos)) < forceThresh:
            print(f)
            particle.tick()
        
        # while particle.pos.x < 20:
        for _ in range(100):
            dst = particle.pos.dst(goldPos)
            f = F(2, 79, dst)
            particle.accelerate(V2(
                f * alphaMass * (particle.pos.x / dst),
                f * alphaMass * (particle.pos.y / dst)
            ))
            particle.tick()
    
    x: list[float] = []
    y: list[float] = []

    for startY, particle in particles.items():
        x.append(startY)
        y.append(degrees(atan(radians(
            (particle.pos.y - goldPos.y) /
            (particle.pos.x - goldPos.x)
        ))))
    
    plt.plot(x, y)
    
    matplotlib.use('TKAgg')
    plt.show()
    


if __name__ == '__main__': main()