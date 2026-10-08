""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import sys
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
import functools
from statistics import mean 
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
from numba import njit

# Exc1
def approximate_pi(n):
    # n is the number of points
    nc=0
    ns=0
    for i in range(n):
        xcor=random.uniform(-1,1)
        ycor=random.uniform(-1,1)
        dist=m.sqrt((xcor**2)+(ycor**2))
        if dist<=1:
            nc+=1
        else:
            ns+=1
    return 4*(nc/n) #add plotting thing?
        

# Exc2, approximation
def sphere_volume(n, d): 
    # n is the number of points     # d is the number of dimensions of the sphere 
    cubeVol=2**d #cube volume (higher dims included)
    nsph=0
    sqr=lambda x:x**2
    for i in range(n):
        corLst=[random.uniform(-1,1) for _ in range(d)] #random dim cordinates
        sqdist=functools.reduce(lambda x,y:x+y,map(sqr, corLst)) #square & sum cordlst
        if sqdist<=1:
            nsph+=1
    return cubeVol*(nsph/n)


#Exc2, real value
def hypersphere_exact(n, d):
    # n is the number of points
    vd=(m.pi**(d/2))/(m.gamma(d/2+1))
    # d is the number of dimensions of the sphere 
    return vd

#Exc3: numba version
@njit
def sphere_volume_numba(n:int, d:int)->float: #simplified spherevolume
    # n is the number of points     # d is the number of dimensions of the sphere 
    cubeVol=2**d #cube volume (higher dims included)
    nsph=0
    for i in range(n):
        sqLst=[]
        for _ in range(d):
            sqLst.append(random.uniform(-1,1)**2)
        sqDist=sum(sqLst)
        if sqDist <=1:
            nsph+=1
    return cubeVol*(nsph/n)
    #np is the number of processes

#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel(n, d, np=10): 
    chunk=n//np
    with future.ProcessPoolExecutor(max_workers=np) as ex:
        futures = [ex.submit(sphere_volume, chunk, d) for _ in range(np)]
        results=[f.result() for f in futures]

    return mean(results)
    # np is the number of processes
    
def main():
    # Exc1
    # dots = [1000, 10000, 100000]
    # for n in dots:
    #     approximate_pi(n)

    # # Exc2
    # n = 100000
    # d = 2
    # print(sphere_volume(n, d))
    # print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # n = 100000
    # d = 11
    # print(sphere_volume(n, d))
    # print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # # Exc3
    # n = 1000000
    # d = 11
    # for i in range(3):
    #     start = pc()
    #     sphere_volume(n, d)
    #     stop = pc()
    #     print(f"Exc3: call# {i+1}, Sequential time of {d} and {n}: {stop-start}")
    # print("What is numba time?")
    # for i in range(3):
    #     start = pc()
    #     sphere_volume_numba(n,d)
    #     stop= pc()
    #     print(f"Exc3: call# {i+1}, Numba Sequential time of {d} and {n}: {stop-start}")

    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    start2 = pc()
    sphere_volume_parallel(n, d)
    stop2 = pc()
    print(f'Exc4: Parallel time of {d} and {n}: {stop2-start2}')
    print("-----------------------------------------------------------")
    

if __name__ == '__main__':
	main()
