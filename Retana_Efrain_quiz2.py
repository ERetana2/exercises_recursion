
"""
@Professor: Olac Fuentes
@Author: Efrain Retana
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

def nested_squares(ax,n,x0,y0,size):
    if n > 1:
        ax.plot([0],[0],linewidth=1.0,color='b')
        p1 = np.array([x0 -size,y0 - size])
        p2 = np.array([x0-size,y0 + size])
        p3 = np.array([x0 + size,y0 +size])
        p4 = np.array([x0 + size,y0 - size])
        points = np.array([p1,p2,p3,p4,p1])
        ax.plot(points[:,0],points[:,1],linewidth=1.0,color='b')
        nested_squares(ax,n-1,x0,y0,size/2)
    
    
def secondary_diagonal(A):
    if len(A) != 0:
        D = []
        for i in range(len(A)):
            D.append(A[i][len(A) - 1 - i])
        return D

def count_occurrences(L,i):
    if len(L) == 0:
        return 0
    if L[0] == i:
        return 1 + count_occurrences(L[1:],i)
    return count_occurrences(L[1:],i)

if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    fig, ax = plt.subplots()
    
    A = np.arange(36).reshape(6,6)
    print(A)
    d = secondary_diagonal(A)
    print(d)  # [5, 10, 15, 20, 25, 30]
    
    L = [3,1,4,6,7,8,9,3,6,2,1,4,5,6]
    print(count_occurrences(L,3))  # 2
    print(count_occurrences(L,6))  # 3
    print(count_occurrences(L,10)) # 0
    
    nested_squares(ax,4,0,0,100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('Retana_Efrain_squares.png')
    

