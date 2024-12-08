import math
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def fractal(l, n, angle): #per a que s'assembli mes a un triangle, n ha de ser gran
    x_dots = []
    y_up = []
    y_mid = []
    y_down = []
   
    for i in range(n):
        x_dots.append(l/(2**i))
        y_up.append(x_dots[i]*np.cos(angle))
        y_mid.append(0)
        y_down.append(-x_dots[i]*np.cos(angle))
        
    x_dots_combined = []
    y_dots_combined1 = []
    y_dots_combined2 = []

    for i in range(n):
        x_dots_combined.append(x_dots[i])
        x_dots_combined.append(x_dots[i])

    for i in range(n):
        y_dots_combined1.append(y_up[i])
        y_dots_combined1.append(0)

    
    for i in range(n):
        y_dots_combined2.append(-y_up[i])
        y_dots_combined2.append(0)


    plt.scatter(x_dots_combined, y_dots_combined1, marker = ".", s = 5, color = 'black')
    plt.plot(x_dots_combined, y_dots_combined1, marker = ".", markersize = 0.5, linewidth = 0.5, color = 'black')   
    
    plt.scatter(x_dots_combined, y_dots_combined2, marker = ".", s = 5, color = 'black')
    plt.plot(x_dots_combined, y_dots_combined2, marker = ".", markersize = 0.5, linewidth = 0.5, color = 'black')

    plt.scatter(x_dots, y_mid, marker = ".", s = 5, color = 'black')

    plt.plot(x_dots, y_up, marker = ".", markersize = 0.5, linewidth = 0.5, color = 'black')

    plt.plot(x_dots, y_down, marker = ".", markersize = 0.5, linewidth = 0.5, color = 'black')


    plt.vlines(x_dots, ymin = y_down, ymax = y_up, linewidth = 0.3, color = "black")
    
    for i in range(1,n):
       plt.fill_between([l/(2**(i-1)), l/(2**(i))], [0,(x_dots[i]*np.cos(angle))], [0,-(x_dots[i]*np.cos(angle))], color = 'black')
               
    plt.show()
    
# if __name__=="__main__":
