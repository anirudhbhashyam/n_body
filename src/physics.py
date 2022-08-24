import os
from pathlib import Path

from dataclasses import dataclass, field

from window import Window
from vec2d import Vec2D
from particle import Particle
from config import Config

class Physics:
    def __init__(self) -> None:
        config = Config(
            Path(__file__, *(2 * [os.pardir]), "config").resolve(),
            ["settings.json"]
        )
        config_data_iter = config.load()
        self.constants = next(config_data_iter)["CONSTANTS"]
    
    def g_acceleration(self, p1: Particle, p2: Particle) -> Vec2D:
        return -(p1.p - p2.p).normalise() * (p2.m * self.constants["G"]) / (p2.p - p1.p).lp_norm(p = 2, radical = False)

    def check_collision_screen(self, p: Particle, screen: Window) -> None:
        if p.p.x < 0:
            p.p.x = 0
            p.v.x *= -1
        elif p.p.x > screen.width:
            p.p.x = screen.width
            p.v.x *= -1
        if p.p.y < 0:
            p.p.y = 0
            p.v.y *= -1
        elif p.p.y > screen.height:
            p.p.y = screen.height
            p.v.y *= -1

    def check_collision_particle(self, p1: Particle, p2: Particle) -> None:
        if (p1.p - p2.p).lp_norm(p = 2, radical = False) <= (p1.r + p2.r):
            p1.v = -p1.v
            p2.v = -p2.v

