from manim import *
import numpy as np
import matplotlib.pyplot as plt
from Project_gpt import fractal 

class Sierpinski(Scene):
    def construct(self):
        # Parameters
        base_length = 8  # Adjust for better visualization in Manim
        depth = 6
        origin_x = -3  # Center the fractal
        origin_y = -3
        angle = np.pi / 3
        beta = 2

        # Generate the fractal
        triangles = fractal(origin_x, origin_y, base_length, angle, beta, depth)
         
        # Add the title with depth and dimension
        dimension=np.log(3)/np.log(2)
        title_text = f"Sierpinski Triangle\nDepth = {depth}\nDimension = {dimension:.10f}"
        title = Text(title_text, font_size=24).to_corner(UL)
        self.play(Write(title))

        # Use a colormap for colors
        colormap = plt.get_cmap("Pastel1", len(triangles))
        for idx, triangle in enumerate(triangles):
            color = colormap(idx % len(triangles))  # Normalize index to [0, 1]
            hex_color = "#" + "".join(f"{int(255 * c):02x}" for c in color[:3])  # Convert to HEX       
            triangle_polygon = Polygon(
                *[(x, y, 0) for x, y in triangle],
                color=hex_color,
                fill_opacity=0.8
            )
            self.play(DrawBorderThenFill(triangle_polygon), run_time=0.1)
            self.wait(0.01)

        self.wait(2)  # Hold the final frame
