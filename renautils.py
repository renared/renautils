# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:00:03 2021

@author: Yann
"""
from math import floor, ceil
import sys
import matplotlib.pyplot as plt

def show(*args, nrows='auto', ncols='auto', title=None):
    ''' 
    Example :
        show(im1, "Image 1", im2, "Image 2", im3, im4, ..., nrows=2, ncols='auto', title="Mes images") 
    '''
    n = len(args)
    for arg in args:
        if type(arg) is str:
            n -= 1
    if nrows=='auto' and ncols=='auto':
        nrows = floor(n**.5)
        ncols = ceil(n**.5)
    elif nrows=='auto':
        nrows = ceil(n / ncols)
    elif ncols=='auto':
        ncols = ceil(n / nrows)
    elif nrows*ncols < n:
        print("show: Not enough cells: defaulting to auto.", file=sys.stderr)
        nrows = floor(n**.5)
        ncols = ceil(n**.5)
        
    if nrows*ncols < n: # occurs when n=3
        nrows+=1
    
    plt.figure()
    
    i=1
    for arg in args:
        if type(arg) is tuple :
            plt.subplot(nrows, ncols, i)
            plt.imshow(arg[0])
            i+=1
            plt.title(arg[1])
            
        elif type(arg) is str :
            plt.title(arg)
        
        else :
            plt.subplot(nrows, ncols, i)
            plt.imshow(arg)
            i+=1
    
    if title!=None:
        plt.suptitle(title)
    
    plt.show()
    
def subplot(*args, nrows='auto', ncols='auto', title=None, show=True):
    ''' 
    Example :
        subplot('plot', (x, y), {'title':'mon plot', 'xlabel':'abscisse', ...}, 'scatter', (x, y), ..., nrows=2, ncols='auto', title="Mes courbes") 
        subplot('imshow', (img,), {'scatter': ([10,42], [26,38])})
    '''
    n = 0 # number of subplots
    nargs = len(args)
    subplot_elms = []
    i = 0
    while i < nargs:
        if args[i] not in ('plot', 'scatter', 'imshow') or i+1 >= nargs or type(args[i+1]) is not tuple:
            raise Exception
        if i+2 < nargs and type(args[i+2]) is dict:
            subplot_elms.append(args[i:i+2+1])
            i = i+3
        else:
            subplot_elms.append(args[i:i+1+1])
            i = i+2
        n += 1
            
    if nrows=='auto' and ncols=='auto':
        nrows = floor(n**.5)
        ncols = ceil(n**.5)
    elif nrows=='auto':
        nrows = ceil(n / ncols)
    elif ncols=='auto':
        ncols = ceil(n / nrows)
    elif nrows*ncols < n:
        print("show: Not enough cells: defaulting to auto.", file=sys.stderr)
        nrows = floor(n**.5)
        ncols = ceil(n**.5)
        
    if nrows*ncols < n: # occurs when n=3
        nrows+=1
    
    plt.figure()
    for i, elm in enumerate(subplot_elms):
        plt.subplot(nrows, ncols, i+1)
        plot_fn_name, plot_args, plot_opt = elm[0], elm[1], {} if len(elm)==2 else elm[2]
        plot = plt.plot if plot_fn_name=='plot' else plt.scatter if plot_fn_name=='scatter' else plt.imshow if plot_fn_name=='imshow' else None
        plot(*plot_args)
        for key in plot_opt:
            fn = getattr(plt, key)
            if type(plot_opt[key]) is tuple:
                fn(*plot_opt[key])
            else:
                fn(plot_opt[key])
                
    if title!=None:
        plt.suptitle(title)
        
    if show:
        plt.show()