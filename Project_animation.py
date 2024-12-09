from manim import *
import numpy as np
from Project_gpt import fractal 

class Sierpinski(Scene):
    def construct(self):
        # Parameters
        base_length = 8  # Adjust for better visualization in Manim
        depth = 4
        origin_x = -3  # Center the fractal
        origin_y = -3
        angle = np.pi / 3
        beta = 2

        # Generate the fractal
        triangles = fractal(origin_x, origin_y, base_length, angle, beta, depth)
        
        # Colors and rendering
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]
        for idx, triangle in enumerate(triangles):
            triangle_polygon = Polygon(
                *[(x, y, 0) for x, y in triangle],
                color=colors[idx % len(colors)],
                fill_opacity=0.5
            )
            self.play(Create(triangle_polygon), run_time=0.1)
            self.wait(0.01)

        self.wait(2)  # Hold the final frame
