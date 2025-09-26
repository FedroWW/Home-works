import numpy as np


arr = np.array([1,2,3])
print(arr)
arr2 = np.array([2,3,4])
matrix = np.stack([arr,arr,arr2])
matrix2 = np.stack([arr,arr2,arr2])
print(matrix, matrix2)
print(matrix*matrix2)
print(matrix@matrix2)


arr = np.array([1,2,3])
print(arr)
arr2=np.array([2,3,4])
print(arr@arr2) #скалярное произведегние

matrix = np.array([arr,arr,arr2])

#Метод наименьших квадратов
x=[1,2,3,4,5]
y=[6,4,4,3,8]

def mnk(x,y):
    x = np.array(x)
    y = np.array(y)
    b = ((x*y).mean() - x.mean()*y.mean())/((x**2).mean() - x.mean()**2)
    a = y.mean() - b*x.mean()
    return a, b
print(mnk(x,y))

arr0=np.zeros(5)
arr1=np.ones(5)
arr1=np.ones(1)*5
print(arr1)
print (arr1+arr0)

arr1 = np.ones((2,2))
print(arr1)
arr2 = np.array([0,1])*0.5
print(arr1+arr2)
# arr2**2 == arr2*arr2
#arr2 = np.ones(2)*5
#print(arr2)
#print(arr1+arr2)