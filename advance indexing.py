import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = arr[[0, 2, 4]]
print(result)   # [10 30 50]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Select specific rows
print(matrix[[ 0,2]]) #(We provide a list of row indices to select rows 0 and 2)
print(matrix[:,[1,2]]) #(We select the first row and the third column)



#boolean indexing
a=np.random.randint(1,100,24).reshape(6,4)
print(a)

print(a>50) #to get the array of boolean values

#to get the numbers which ae greater than 50
print(a[a>50]) #super imp
print(a[(a%2==0) & (a>50)]) # combining logicsss

#broadcasting  RULES
#1  Make the arrays of same number of dimensions
#   (3,3,3) and (3) -> (3,3,3) and (1,1,3)
#2  Make each dimension  of the two array of same type
#     dimension wit size 1 is stretched to match the other array


#sigmoid
def sigmoid(x):
    return 1/(1+np.exp(-x))


a=np.array(20)
sigmoid_a=sigmoid(a)
print(sigmoid_a) 



#mean squared error
actual=np.random.randint(1,100,25)
predicted=np.random.randint(1,100,25)
print(actual)
print(predicted)
mse=np.mean((actual-predicted)**2) # how mean squared error is calculated
print(mse)

#how to deal with missing values
a=np.array([1,2,3,np.nan,5,6,np.nan])
print(a)
#to check where the nan values are present
print(np.isnan(a))
print(~(np.isnan(a))) # to get the boolean values where nan is not present
      
     
      
#plotting graphs using numpy
#PLOTTING STRAIGHT LINE
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y = x 
print(plt.plot(x,y))


#PLOTTING PARABOLA
x=np.linspace(-10,10,100)
y=x**2
print(plt.plot(x,y))

#PLOTTINH EXPONENTIAL CURVE
x=np.linspace(-10,10,100)
y=np.sin(x)
print(plt.plot(x,y))


#PLOTTING LOGARITHMIC CURVE
x=np.linspace(-10,10,100)
y=(x*(np.log(x)))
print(plt.plot(x,y))




      
      




