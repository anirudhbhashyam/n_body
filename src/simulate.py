import os
import sys
import pygame
from pathlib import Path

import numpy as np

from dataclasses import dataclass, field

from window import Window
from particle import Particle
from vec2d import Vec2D
from assets import Assets
from physics import Physics

@dataclass
class Simulate:
    window: Window = field(
        default_factory = Window
    )
    
    n: int = field(
        default = 2
    )
    
    particles: list[Particle] = field(
        default_factory = list
    )
    
    time_step: float = field(
        default = 1e6
    )
    
    timer: pygame.time.Clock = field(
        default_factory = pygame.time.Clock
    )
    
    fps: int = field(
        default = 60
    )

    assets: Assets = field(
        init = False
    )

    physics: Physics = field(
        default_factory = Physics
    )
    
    def __post_init__(self) -> None:
        pygame.init()
        self.assets = Assets(Path(__file__, *(2 * [os.pardir]), "res").resolve())
        self.background = pygame.transform.scale(
            self.assets.images["background"], 
            (self.window.width, self.window.height)
        ).convert()

        if len(self.particles) == 0:
            self.particles = [
                Particle.generate_particle() for _ in range(self.n)
            ]

        self.n = len(self.particles)
        
    def run(self) -> None:
        running = True
        while running:
            self.timer.tick(self.fps)
            self.window.render_pixels(self.background, (0, 0))
            
            for particle in self.particles:
                particle.draw(self.window.screen)
                net_acceleration = Vec2D()
                for particle_ in self.particles:
                    if particle_ != particle:
                        net_acceleration += self.physics.g_acceleration(particle, particle_)

                particle.update(
                    net_acceleration, 
                    self.time_step,
                    self.window
                )
                self.physics.check_collision_screen(particle, self.window)
                        
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                    
            # sim_count += 1
                    
                    
        
