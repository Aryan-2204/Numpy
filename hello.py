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






a=np.ones((3,1)) #array of ones
print(a)






z= np.zeros((2,3)) #array of zeros
print(z)







b=np.random.random((2,3))#random numbers in 2 rows and 3 columns
print(b)






v=np.linspace(0,1,5) #5 values between 0 and 1
print(v)





d=np.identity(3) #identity matrix of size 3
print(d)


a1= np.arange(1,10).reshape(3,3)
print(a1)
print(a1.ndim)#number of dimensions
print(f.ndim)

#Array Properties

print(a1.shape)
print(f.shape)#dimensions of the array

print(a1.size)
print(f.size)
print(d.size)#number of elements in the array



print(a1.dtype)# int64= 8 bytes,int32=4 bytes , float32=4 bytes,float64=8 bytes
print(a1.astype(np.int32))#changing data type to int32

#Array Operations
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

a1=a1*2 #scalar multiplication
print(a1)
a2 =a2+3 #scalar addition
print(a2)


#relational operations
print(a2>5) #itemwise comparison

#vectorized operations
print(a1+a2)    #since shape is same
print(a2-a1)
print(a1*a2)

#functions

a1=np.random.random((2,3))
a1=np.round(a1*100) #scaling and rounding
print(a1)
c=np.max(a1)
print(c)

b=np.sum(a1)
print(b)

#coloum =0 an row =1   
d=np.sum(a1,axis=1)
e=np.mean(a1,axis=1)
f=np.median(a1,axis=1)
g=np.std(a1,axis=1)
print(d)
print(e)
print(f)
print(g)


#dot product (columns of first matrix should be equal to rows of second matrix)
a2=np.arange(12).reshape(4,3)
a3=np.arange(12,24).reshape(3,4)
print(a3)
d=np.dot(a2,a3)
print(d)


#log and exp
a=np.log(a2)
print(a)
b=np.exp(a3)
print(b)


np.floor(a3) #rounding down
np.ceil(a3)  #rounding up
print(np.floor(a3)) 
print(np.ceil(a3))




#indexing and slicing
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a2)
print(a2[1,2]) #2nd row and 3rd column

print(a3)
print(a3[1,0,1])# 2nd block,1st row,2nd column


#slicing :
print(a2[:,2]) #all rows and 3rd column
print(a2[1,:]) #2nd row and all columns
print(a2[1:,1:3])#2nd and 3rd rows and 2nd and 3rd columns
print(a2[::2,::3])# alternate rows and alternate columns

print(a2[::2,1::2])# alternate rows and columns starting from 2nd column
print(a2[::2,::3])# alternate rows and columns starting from 1st column



print(a3[0,1,:]) #1st block,2nd row,all columns
print(a3[1,:,1]) #2nd block,all rows,2nd column


#iterations
#in 1 d all items in 2d all rows and in 3d all 2d arrays will be print in simple for loop
for i in np.nditer(a3): #(to print all elements in the array3D)
    print(i)
 
 
#transpose -> rows interchange by columns and vica versa
a2=np.arange(12).reshape(3,4)
print(a2)
print(a2.T)   #transpose of matrix

#ravel
print(a3.ravel())#converting multi dimensional array to 1D array


a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
np.hstack((a4,a5))#horizontal stacking
print(np.hstack((a4,a5)))
print(np.vstack((a4,a5)))#vertical stacking
  
print(np.hsplit(a4,2))#horizontal splitting into 2 arrays
print(np.vsplit(a4,3))#vertical splitting into 2 arrays