import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 20, 255)
    j0 = first_bessel_func(x)
    j1 = first_bessel_func(x)/x-np.cos(x)/x
    j2 = (3*sec_bessel_func(x)-first_bessel_func(x))/2
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x, j0, label='j0')
    ax.plot(x, j1, ':', label='j1')
    ax.plot(x, j2, '--', label='j2')
    ax.set_xlim(0, 20)
    ax.axhline(color="grey", zorder=-1)
    ax.legend(loc="upper right", title='legend')
    
    
def first_bessel_func (x):
    y=[]
    for xx in x:
        if xx == 0.0:
            y+=[1]
        else:
            y+=[np.sin(xx)/xx]
    return np.array(y)
            
    
def sec_bessel_func(x):
    y=[]
    for xx in x:
        if xx == 0.0:
            y+=[1]
        else:
            y+=[np.sin(xx)/(xx*xx) - np.cos(xx)/xx]
    return np.array(y)
    
    
def third_bessel_func(x):
    y=[]
    a = 3
    for xx in x:
        if xx == 0.0:
            y+=[1]
        else:
            y+=[(((3/xx**2)-1)*(np.sin(xx)/a))-(3*np.cos(xx))/xx**2]
    return np.array(y)

main()