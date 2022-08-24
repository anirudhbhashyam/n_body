import os
from pathlib import Path

from dataclasses import dataclass, field

from numpy.random import default_rng

import pygame

from vec2d import Vec2D
from window import Window
from config import Config

@dataclass
class Particle:
    p: Vec2D = field(
        default = Vec2D()
    )
    
    v: Vec2D = field(
        default = Vec2D()
    )
    
    m: float = field(
        default = 4.0
    )

    r: float = field(
        init = False
    )

    color: tuple[int, int, int] = field(
        default = (255, 255, 255),
        repr = False
    )
    
    def __post_init__(self) -> None:
        # Set the radius proportional to the mass.
        self.r = self._generate_radius(self.m)
        config = Config(
            Path(__file__, *(2 * [os.pardir]), "config").resolve(),
            ["settings.json"]
        )
        config_data_iter = config.load()
        self.constants = next(config_data_iter)["CONSTANTS"]

    @staticmethod
    def _generate_radius(mass: float) -> float:
        return 4 * mass ** (1 / 4)
    
    def draw(self, screen: Window) -> None:
        pygame.draw.circle(screen, self.color, (self.p.x, self.p.y), self.r)
   
    def update(self, net_acceleration: float, time_step: float, screen: Window) -> None:
        self.v += net_acceleration * time_step 
        self.p += self.v * time_step

    @classmethod
    def generate_particle(cls):
        p = Vec2D(
            default_rng().integers(0, Window.width  - 10),
            default_rng().integers(0, Window.height - 10),
        )
        v = Vec2D(
            (1e-4 - 1e-6) * default_rng().random() + 1e-6,
            (1e-4 - 1e-6) * default_rng().random() + 1e-6,
        )
        m = (2.0 - 1e-1) * default_rng().uniform() + 1e-1
        r = cls._generate_radius(m)
        color = default_rng().integers(0, 255, size = 3)
        return cls(
            p = p,
            v = v,
            m = m,
            color = color,
        )
        
        
        