import numpy as np
a= np.array([123]) #vector
print(a)


import numpy as np
b=np.array([[1,2,3],[4,5,6]]) #matrix
print(b)

import numpy as np
c=np.array([[[1,2],[3,4],[5,6]]])#tensor
print(c)

d=np.array([1,2,3], dtype='float32') #specifying data type
print(d)


e=np.arange(1,11,2) #another method to print array
print(e)

f=np.arange(1,11).reshape(5,2)#reshaping 5 col,2 rows
print(f)

