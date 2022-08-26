import numpy as np
from time import time

a=np.empty((1000,1000),dtype=np.ndarray)
for i in range(1000):
    for j in range(1000):
        a[i][j]=np.random.randint(2,size=(2))
        
        
b=np.empty((2,2),dtype=np.ndarray)
for i in range(2):
    for j in range(2):
        b[i][j]=np.random.randint(2,size=(2))
 

# A represents bigger matrix B represents smaller matrix
# Here M and N represent rows and columns of bigger matrix respectively
# and m and n represent rows and columns of smaller matrix respectively
def SearchSubMatrix(A,B,M,N,m,n):
    start_time=time()
    if M<m or N<n:
        end_time=time()
        print(f"Total time taken by execution is {start_time-end_time}")
        return (-1,-1)
    answer =[]

    for i in range(0,M-m+1): 

        for j in range(N-n+1):
            found = True
            if np.array_equal(A[i][j],B[0][0]):
                for r in range(0,m): 
                    for s in range(0,n):
                        if np.array_equal(B[r][s],A[r+i][s+i])==False:
                            found = False
                            break 

                if found:
                    answer.append((i,j))
                    break 
    end_time=time()
    print(f"Toatal time taken is :{end_time-start_time}")
    return answer
print(SearchSubMatrix(a,b,1000,1000,2,2))
