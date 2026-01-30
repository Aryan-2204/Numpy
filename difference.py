#numpy is faster than lists for numerical operations because it uses contiguous memory allocation and optimized C libraries.

#   HOW IS NUMPY BETTER THAN LIST? // list can store non homogenous data

#speed comparison

#in list    
import numpy as np
import time
a=[i for i in range(100000000)]
b=[i for i in range(100000000,200000000)]

c=[]

start=time.time()
for i in range (len(a)):
    c.append(a[i]+b[i])
   # print(time.time()-start)
      
#In numpy   
c=np.arange(100000000)
d=np.arange(100000000,200000000)
start=time.time()  
a=c+d
print(time.time()-start)  

#memory usage comparison
   
   
#in list  (space was earlier same as numpy but now we are using int16 in numpy to reduce space)
z= [i for i in range(100000000)]
import sys
print(sys.getsizeof(z))

#in numpy(reduce space)
y=np.arange(100000000,dtype=np.int16)
print(sys.getsizeof(y))
    
#convinence wise numpy is better    
    
    