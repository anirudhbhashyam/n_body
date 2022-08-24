import os
import sys
import argparse
from pathlib import Path 

sys.path.append(str(Path("src").resolve()))

from vec2d import Vec2D
from simulate import Simulate
from particle import Particle

def process_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = "Simulate a particle system."
    )
    
    parser.add_argument(
        "-n",
        "--n_particles",
		type = int,
		help = "Number of particles",
        default = 2
	)
    
    return parser.parse_args()

def main() -> None:
    args = process_args()

    # particles = [
    #     Particle(p = Vec2D(200, 200), m = 4.0, v = Vec2D(1e-6, -1e-6)),
    #     Particle(p = Vec2D(400, 200), m = 5.0, v = Vec2D(1e-6, -1e-6)),
    #     Particle(p = Vec2D(400, 400), m = 8.0, color = (255, 0, 0))
    # ] 
    
    sim = Simulate(n = args.n_particles, time_step = 1e4) 
    sim.particles.append(Particle(p = Vec2D(200, 200), m = 8.0, v = Vec2D(1e-6, -1e-6), color = (255, 0, 0)))
    sim.run()
    
if __name__ == "__main__":
    main()