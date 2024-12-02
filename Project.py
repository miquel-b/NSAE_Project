import math
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def fractal(l, n, angle): #per a que s'assembli mes a un triangle n ha de ser gran
    x_dots = [-l]
    y_up = [x_dots[0]*np.cos(angle)]
    y_mid = [0]
    y_down = [-x_dots[0]*np.cos(angle)]
   
    for i in range(1,n):
        x_dots.append(-l/(2*i))
        y_up.append(x_dots[i]*np.cos(angle))
        y_mid.append(0)
        y_down.append(-x_dots[i]*np.cos(angle))
    # return (x_dots, y_dots, y_dots1, y_dots2)
    # return x_dots
    x_dots_combined = []
    y_dots_combined1 = []
    y_dots_combined2 = []

    for i in range(n):
        x_dots_combined.append(x_dots[i])
        x_dots_combined.append(x_dots[i])

    for i in range(n-1):
        y_dots_combined1.append(0)
        y_dots_combined1.append(y_up[i+1])
    
    for i in range(n-1):
        y_dots_combined2.append(0)
        y_dots_combined2.append(-y_up[i+1])
        
    x_dots_combined.pop(0)
    #maybe if statement:
    y_dots_combined1.append(0)
  
    y_dots_combined2.append(0)

    

    plt.scatter(x_dots_combined, y_dots_combined1, marker = ".", s = 5)
    plt.plot(x_dots_combined, y_dots_combined1, marker = ".", markersize = 2.5, linewidth = 0.5)    
    plt.scatter(x_dots_combined, y_dots_combined2, marker = ".", s = 5)
    plt.plot(x_dots_combined, y_dots_combined2, marker = ".", markersize = 2.5, linewidth = 0.5)    

    # plt.scatter(x_dots, y_dots, marker = ".", s = 5)
    plt.scatter(x_dots, y_mid, marker = ".", s = 5)
    # plt.scatter(x_dots, y_dots2, marker = ".", s = 5)
    plt.plot(x_dots, y_up, marker = ".", markersize = 2.5, linewidth = 0.5)
    # plt.plot(x_dots, y_dots1, marker = ".", markersize = 2.5)
    plt.plot(x_dots, y_down, marker = ".", markersize = 2.5, linewidth = 0.5)
        # plt.plot((x_dots[0], -y_dots2[0]), (x_dots[1], 0), linestyle = "-", marker = ".", markersize = 2.5, linewidth = 0.5)

    plt.vlines(x_dots, ymin = y_down, ymax = y_up, linewidth = 0.3, color = "red")
    
    # for i in range(n):
    # plt.fill_between(x_dots, y_up, y_down)
    
    plt.fill_between([-1, -0.5], [0, 0.25], [0, -0.25])
    plt.fill_between([-0.5, -0.25], [0, 0.125], [0, -0.125])
    # plt.fill_between(x_dots, y_dots_combined2, y_dots_combined1)
    
    plt.show()
    
    return x_dots,y_up, y_down, x_dots.shape()
# (x_dots_combined,
#         y_dots_combined1,
#         y_dots_combined2, x_dots)

# x = [-1,-0.5,-0.5,-0.25,-0.25,-0.125, -0.125]
# y = [0,-0.5, 0,  -0.25, 0,   -0.125,  0]
# plt.scatter(x, y, marker = ".", s = 5)
# plt.plot(x, y, marker = ".", markersize = 2.5, linewidth = 0.5) 

# if __name__=="__main__":
    
