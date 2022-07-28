import numpy as np #import library numpy as np
n = int(input("Enter size for square matrix : "))
A = np.ones(n*n).reshape((n, n)) #เพิ่มค่า 1  ให้กับทุกค่าใน matrix 
for i in range(0,n):  
    for j in range(0,n):
        if (i < j and j != n):
            A[i,j] = 0
        elif (i == j or j == n):
            A[i,j] = 1
        else :
            A[i,j] = -1
print(A)


"""
Enter size for square matrix : 4
[[ 1.  0.  0.  0.]
 [-1.  1.  0.  0.]
 [-1. -1.  1.  0.]
 [-1. -1. -1.  1.]]
"""