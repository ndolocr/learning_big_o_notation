"""
O(2^n)
We are entering dangerous waters here, in interviews and in implementation we want to avoid a 
situation where the time complexity of our algorithm reaches O(2^n) as it denotes an algorithm 
whose growth doubles with each addition to the input data set.

The growth of this algorithm is exponential, let’s say we have n=2 inputs, then it will perform 
4 times, with n=3, it will perform operations 8 times and so on.

In the example if the input parameter n is given the value of 10, then it will perform operations 2^10 
times which is 1024 times.
"""

from datetime import datetime

start_time = datetime.now()

def exponential(n):
    for x in range(1, 2**n):
        if x%20==0:
            print(x)
        print(x, end=", ")

exponential(100)

print()
end_time=datetime.now()
duration = end_time - start_time
print(f"Duration taken is {duration}")