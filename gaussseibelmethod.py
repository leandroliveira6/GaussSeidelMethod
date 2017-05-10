# -*- coding: utf-8 -*-
"""
Created on Wed May 10 02:11:47 2017

@author: Leandro
"""

import numpy as np

def gaussseibel(A,b,x0,N,TOL):
    n = len(A)
    k = 1
    while (k <= N):
        x = np.zeros(n)
        for i in range(n):
            s = 0.0;
            for j in range(i):
                s += A[i,j]*x[j]
            for j in range(i+1,n):
                s += A[i,j]*x0[j]
            x[i] = (b[i] - s)/A[i,i]
        if (np.linalg.norm(x-x0) < TOL):
            return x,k
        k += 1;
        x0 = np.copy(x)
    return x0,k

A = np.array([[1.,-1.,0.],\
              [-1.,2.,1.],\
              [0.,1.,5.]])
b = np.array([3.,-3.,4.])
guess = np.array([0.,0.,0.])
x,n = gaussseibel(A,b,guess,100,0.00000001)
print("GauSei = {} em {} iterações.".format(x.round(2), n))
