"""
Solutions to module 1
Student: 
E-mail:
Reviewed by:Shengkai
Review date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have test code running at the top level (i.e. outside the main function),
you have to remove it before uploading your code into Studium!
Also remove any trace and debugging printouts!

You may not import any packages other than time and math. These may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documentation and and don't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """Exc1: Computes m*n using additions"""
    if n == 0:
        return 0
    elif n>0:
        return m + multiply(m, n - 1)
    elif n<0:
        return -m + multiply(m, n+1)


def harmonic(n: int) -> float:              
    """Exc2: Computes and returns the harmonic sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1
    return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:              
    """Exc3: Returns the binary representation of x"""
    if x<0:
        return "-" + get_binary(-x)
    if x==0:
        return "0"
    if  x==1:
        return "1"
    return get_binary(x//2) + f"{x%2}"


def reverse_string(s: str) -> str:        
    """Exc4: Returns the string s reversed """
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


def largest(a: list):
    """Exc5: Returns the largest element in a"""
    if len(a)==1:
        return a[0]
    elif a[0]<=a[-1]:
        return largest(a[1:])
    else:
        return largest(a[:-1])



 
def count(x, s: list) -> int:                
    """Exc6: Counts the number of occurences of x on all levels in s"""
    if len(s)==0:
        return 0
    elif x == s[0]:
        return 1 + count(x, s[1:])
    elif type(s[0])==list:
        return 0 + count(x,s[0]) + count(x,s[1:])
    elif x != s[0]:
        return 0 + count(x, s[1:])


def bricklek(f: str, t: str, h: str, n: int) -> list[str]:
    """Exc7: Returns a list of string instructions for how to move the tiles"""
    if n==0:
        return []
    else:
        return  bricklek(f, h, t, n-1) + [f"{f}->{t}"]+ bricklek(h, t, f, n-1)


def fib(n: int) -> int:                      
    """For Exc9: Returns the n:th Fibonacci number"""
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n):
    memory = {0:0, 1:1}

    def _fib_mem(n):
        if n not in memory:
            memory[n] = _fib_mem(n-1) + _fib_mem(n-2)
        return memory[n]
    
    return _fib_mem(n)

def main():
    print('\nCode that demonstrates my implementations\n')
    print(multiply(-3,-4))
    print('\n\nCode for analysing fib and fib_mem\n')
    runtimes=[]
    for i in range(25,35):
        start=time.perf_counter()
        fib(i)
        end=time.perf_counter()
        runtime=end - start
        print(runtime)
        runtimes+=[runtime]
        i+=1
    print(runtimes)
    runtime_comp=[]
    for i in range(1,10):
        print(runtimes[i]/runtimes[i-1])
        comp=runtimes[i]/runtimes[i-1]
        runtime_comp+=[comp]
        i+=1
    print(f"average: {sum(runtime_comp)/len(runtime_comp)}")
    start_fib_mem=time.perf_counter()
    fib100=fib_mem(100)
    end_fib_mem=time.perf_counter()
    elapsed=end_fib_mem-start_fib_mem
    print(f"\nfib_mem(100)={fib100}, elapsed time={elapsed}s")
    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the non-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  antalet drag beräknas genom: 2^n -1 så för 50 brickor blir det 2^50 -1 =1,126 *10^15 sekunder
  =35 702 051 exclusive skottår
  ca 35 702 000 år
  
  
  
  Exercise 9: Time for Fibonacci:
a)  time(fib(i+1))/time(fib(i)) ger för högre värden på i ett värde närmare 1,618 (main)
b)fib(50) = fib(35)*1,618^(50-35)
fib(35) tar 0,791 sekunder på min dator, fib 50 borde därför ta ca 0,719*1,618^15
 = 980 sekunder= ca 16 minuter
 fib(100) blir då 0,791*1,618^65 = 961 553 år = 961 tusen år
  
  
  Exercise 10: Time for fib_mem:
fib(100) är =354 224 848 179 261 915 075 = 354 224 848 biljoner (trillion)
det tog 7,98e-05 sekunder
  
  
  Exercise 11: Comparison sorting methods:
t(n)=c*f(n) => c=t(n)/f(n)
för instick:
c=t/(n^2)=1/(1000^2)=10^-6 s
för merge:
c=t/(nlogn)=1/(1000*log1000)=1/3000=3,3*10^-4 s

10^6:
instick:    t(n)=10^-6 * (10^6)^2                   =1 000 000 s = 11,57 dagar
merge:      t(n)=3,3*10^-4 * (10^6 * log(10^6))     =1 980 s     = 33 min   
10^9
instick:    t(n)=10^-6 * (10^9)^2                   =1 000 000 000 000 s= 31 709 år
merge:      t(n)=3,3*10^-4 * ((10^9)*log(10^9))     = 34,7 dagar
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
B: t(n)=1 då n=10 ger c= 1/(10*log10) => c=1/10
A: t(n)=c*f(n) => 1 = 1*n 

t(n)A=1*n
t(n)B=1/10 * nlog(n)
t(n)A<t(n)B => 1*n < 1/10 * nlog(n) => n>10^10



  
"""
