import numpy as np
import matplotlib.pyplot as plt

def fractal(ox, oy, l,angle,beta, depth):
    """
    Recursive function to generate the points for the Sierpinski triangle.
    
    Parameters:
    - ox, oy: Origin coordinates of the triangle.
    - l: Length of the base of the triangle.
    - depth: Number of recursive iterations.
    
    Returns:
    - List of (x, y) points that form the Sierpinski triangle.
    """
    if depth == 0:
        # Base case: Draw a single triangle
        half_length = l / beta
        height = (np.cos(angle/2)) * l
        points = [
            (ox, oy),  # Bottom-left
            (ox + l, oy),  # Bottom-right
            (ox + half_length, oy + height),  # Top
            (ox, oy)  # Close the triangle
        ]
        return [points]
    else:
        # Recursive case: Divide into 3 smaller triangles
        half_length = l / beta
        height = (np.cos(angle/2)) * half_length
        triangles = []
        # Bottom-left triangle
        triangles += fractal(ox, oy, half_length,angle,beta, depth - 1)
        # Bottom-right triangle
        triangles += fractal(ox + l*(beta-1)/beta, oy, half_length,angle,beta,depth - 1)
        # Top triangle
        triangles += fractal(ox + (l*(beta-1)/beta)*np.cos(angle), oy + height, half_length,angle,beta, depth - 1)
        return triangles

def plot_sierpinski(triangles, colors):
    """
    Plot the generated Sierpinski triangles.

    Parameters:
    - triangles: List of triangle points to plot.
    - colors: Colormap for the triangles.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    for idx, triangle in enumerate(triangles):
        x, y = zip(*triangle)  # Unzip into x and y
        ax.plot(x, y, color=colors[idx % len(colors)])
        plt.pause(0.05)
    ax.set_aspect('equal')
    ax.axis('on')  # Hide axes for a cleaner look
    plt.title("Sierpinski Triangle")
    plt.show()

if __name__ == "__main__":
    # Parameters
    base_length = 10  # Length of the base of the initial triangle
    depth = 6  # Number of iterations
    origin_x = 0  # Starting x-coordinate
    origin_y = 0  # Starting y-coordinate
    angle=np.pi/3
    beta=2
    colors = plt.cm.viridis(np.linspace(0, 1, depth * 3))  # Generate color gradient

    # Generate the Sierpinski triangle
    triangles = fractal(origin_x, origin_y, base_length,angle,beta,depth)

    # Plot the result
    plot_sierpinski(triangles, colors)
