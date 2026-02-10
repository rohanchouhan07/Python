import numpy as np

arr=np.array([[1,2,3,5],[10,20,30,40]])
new_arr=np.insert(arr,1,[5,15,25,35],axis=0)
print(new_arr)