#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Define function that creates the base points of the triangle, it can be called any time a set of triangles is to be created
def fractal(l0,l,a):
    px=[l0]
    py=[0]
    px.append(l0-l*np.cos(a))
    py.append(l*np.sin(a))
    px.append(l0-l*np.cos(-a))
    py.append(l*np.sin(-a))
    px.append(px[0])
    py.append(py[0])
    return px,py

#runs script normally, it allows the function above to be called as an import function
if __name__=="__main__":
    #Create a set of 4 angles 
    a=np.linspace(np.pi/3,np.pi/2,4,endpoint=True)
    l=1
    l0=1
    iter=7 #number of iterations (sub triangles to create
    colors = matplotlib.colormaps['Dark2'].colors # Basic colors used in plotting
    
    fig1, ax = plt.subplots() #First figure all of the triangles toghether
    for ind,ai in enumerate(a): #Creation of diferent triangles with ai angles
        px=[]
        py=[]
        l=1
        l0=1
        for i in range(iter):
            x,y=fractal(l0,l,ai)
            px.append(x)
            py.append(y)
            l=l/2
    
        for j in range(len(px)): #Plotting of first figure
            if j==len(px)-1:
                ax.plot(px[j],py[j],'--.',color=colors[ind],label=f"angle={ai/np.pi:.2f}*pi")
            else:
                ax.plot(px[j],py[j],'--.',color=colors[ind],)
    
        ax.grid(True)
        ax.set_title(f"Fractal angle variable")
        ax.legend()
    fig1.tight_layout()
    
    fig2,bx = plt.subplots(4) #Second figure Diferent fractals separated
    
    for ind,ai in enumerate(a):
        px=[]
        py=[]
        l=1
        l0=1
    
        for i in range(iter):
            x,y=fractal(l0,l,ai)
            px.append(x)
            py.append(y)
            l=l/2
    
        for j in range(len(px)):
            bx[ind].plot(px[j],py[j],'--.',color=colors[ind],)
        bx[ind].grid(True)
        bx[ind].set_title(f"Fractal angle={ai/np.pi:.2f}*pi")
    
    fig2.tight_layout()
    plt.show()
    
