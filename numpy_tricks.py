import numpy as np
#sort()
a=np.random.randint(1,100,10)
print(np.sort(a)) # sorting array in ascending order
b=np.random.randint(1,100,10).reshape(5,2)
print(np.sort(b,axis=0))#coliumn wise sorting
print(np.sort(a[::-1]))# sorting in descending order

#append() - add at the end 
print(np.array(a) + 200)
print(np.append(b, np.ones((b.shape[0], 1)), axis=1))


#concatenate
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d),axis=0)) #row wise

#umique()
print(np.unique(a)) #gives unique elements in sorted order

#np.expands_dims()
np.expand_dims(a,axis=0) # adds an axis at specified position
print(a.shape) #to make column vector ,column vector
np.expand_dims(a,axis=1)
print(a.shape)  # (1, 10)

#where()
print(np.where(a>50,a,0)) #gives indices where condition is true
#where(condition,true,false)

#argmax()
print(np.argmax(a)) #gives index of maximum element
print(np.argmax(b,axis=0)) #gives index of maximum element column wise

#argmin()
print(np.argmin(a)) #gives index of minimum element
print(np.argmin(b,axis=1)) #gives index of minimum element row wise


#cumsum()- cumulative sum
print(np.cumsum(b,axis=0)) #cumulative sum of elements in array    

#cumprod()
print(np.cumprod(b,axis=1))

#percentile
print(np.percentile(a,100))

#histogram- gives frequency count in given range
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))



#corrcoef- {how much the two qauntities are co-related}
salary=np.array([2000,3000,4000,5000,6000])
experience=np.array([1,2,3,4,5,])
print(np.corrcoef(salary,experience))

#isin
items=[10,20,30,40,50]
print(np.isin(a,items))# to find if items are present in array (a)

#flips
print(np.flip(a)) #creates a mirror image works on 2D as well

print(np.flip(b)) #flips row and column but can do singly by proviidng axis

#put (edits in array)
print(np.put(a,[0,1],[10,40]))

#delete (returns new array after deletion)

print(np.delete(a,0))


#set functions

#union
m= np.array([1,2,3,4,5,6,7,4])
n=np.array([1,3,4,5,67,8,4])

print(np.union1d(m,n))

print(np.intersect1d(m,n))

print(np.setdiff1d(m,n)) # present in m but not n

print(np.setxor1d(m,n)) #removes common

#print(np.in1d(m,10))# searches if present in m

#clip - keeps values in range
print(np.clip(a,a_min=35,a_max=75))