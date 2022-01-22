from vector import *
from dataclasses import dataclass

@dataclass
class Particle:
    pos: V2
    vel: V2

    def tick(self):
        self.pos += self.vel
    
    def accelerate(self, Δv: V2):
        self.vel += Δv