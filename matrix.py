import numpy as np
def count(start,step):
    while True:
        yield start
        start+=step
size1 = int(input("d1"))
size2 = int(input("d2"))

np_matrix = np.zeros((size1,size2))
column_list = list(range(size2))
fill = count(1,1)

np_matrix[0,0]= 1
for i,j in enumerate(list(range(size1,size2))):
    if(np_matrix[i-1,j+1] ==0):
        np_matrix[i-1,j+1]= next(fill)
    else:
        np_matrix[i+1,j]= next(fill)
print(np_matrix)