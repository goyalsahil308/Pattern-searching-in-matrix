# Pattern-searching-in-matrix

## Searching a certain pattern in a matrix of 1000 by 1000 where each element is a numpy array 
First created a empty numpy array of 1000 *1000  

    a=np.empty((1000,1000),dtype=np.ndarray)
    
Then filled array with numpy arrays
  
      for i in range(1000):
  
        for j in range(1000):
     
            a[i][j]=np.random.randint(2,size=(2))
            
###  SearchSubMatrix(A,B,M,N,m,n)

where A represents matrix in which we want to search our pattern <br />
B represents matrix which we want to search <br />
M represents rows of bigger matrix <br />
N represents columns of bigger matrix <br />
m represents rows of smaller matrix <br />
n represents column of smaller matrix <br />

    if M<m or N<n:
        return (-1,-1)
        
if matrix A is smaller than matrix B it will return (-1,-1)

        
In matrix A ,search for the first element of matrix B. When we find the first element, then compare the other elements of matrix B. with elements of matrix A . If correctly 
found it will put indexes of matrix B in list 'answer'. 
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
       



        
