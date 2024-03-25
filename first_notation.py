"""
O(1)

The first Big O Notation that we have is O(1), 
it simply means that the operation will always 
execute in a constant amount of time regardless 
of how big the input size is.

In the example, the function is simply logging 
an element of the given array in the console. How 
many operations does this function take if the size 
of the array is increased to 1,000 or let’s say a 100,000?

Since we are just grabbing a single element inside the array, 
no matter how big the array size gets, the time it takes always 
remains constant or O(1).
"""
from datetime import datetime

start_time = datetime.now()
# given_list = [1,2,3,4,5,6,7,8,9,10]
# given_list = [1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,]
# given_list = [1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 
# 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,]

given_list = [1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 
              1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,
              2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 
              1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,
              2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 
              1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,
              2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 
              1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 
              1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,
              3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,
              3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,
              5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,
              5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
              9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,
              1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,]
print(given_list[208])
end_time=datetime.now()
duration = end_time - start_time
print(f"Duration taken is {duration}")