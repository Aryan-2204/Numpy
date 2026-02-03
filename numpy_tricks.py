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

#cumsum()





