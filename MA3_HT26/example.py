import random
import math as m
import functools
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future

def runner(n):
    print(f"Performing a costly function {n}")
    pause(n)
    print(f"Function {n} complete")

def sq(x):
    return x**2

# for x in map(sq, [2,3,4,5]):
#     print(x)

# with future.ProcessPoolExecutor() as ex:
#     p1=ex.submit(runner)
#     p2=ex.submit(runner)
#     r1=p1.result()
#     r2=p2.result()
# print("all done")

if __name__ == "__main__":
    start=pc()
    with future.ProcessPoolExecutor() as ex: #or ThreadPool
        p= [5,4,3,2,1]
        results=ex.map(runner,p)
        for r in results:
            print(r)
    end=pc()
    print(f"Process took {round(end-start, 2)} seconds")
