# import warnings
import numpy as np
from time import time
# np.set_printoptions(threshold=np.inf)               # prints the full aray
# warnings.simplefilter(action='ignore', category=FutureWarning)  # Ignore warnings

# a=None
a=np.empty((1000,1000),dtype=np.ndarray)    # Create empty numpy array of 1000 * 1000
for i in range(1000):
    for j in range(1000):
        num=np.random.randint(2,size=(2,2))         # Fill the array with random arrays of 2 * 2 conatinings random integars from range 0 to 99
        a[i][j]=np.asmatrix(num)


# b=None
b=np.empty((2,2),dtype=np.ndarray)
for i in range(2):
    for j in range(2):
        num=np.random.randint(2,size=(2,2))
        b[i][j]=np.asmatrix(num)

# To test the time taken by algo to search pattern which is present at the last of array
# a[997][995]=np.array([
#     [67,57],
#     [19,56]])
# a[997,996]=np.array([
#     [7,58],
#     [9,46]])  
# a[998,995]=np.array([
#     [77,47],
#     [34,34]])
# a[998,996]=np.array([
#     [2,66],
#     [78,45]])


# b[0][0]=np.array([
#     [67,57],
#     [19,56]])
# b[0][1]=np.array([
#     [7,58],
#     [9,46]])  
# b[1][0]=np.array([
#     [77,47],
#     [34,34]])
# b[1][1]=np.array([
#     [2,66],
#     [78,45]])



# A represents bigger matrix B represents smaller matrix
# Here M and N represent rows and columns of bigger matrix respectively
# and m and n represent rows and columns of smaller matrix respectively
def SearchSubMatrix(A,B,M,N,m,n):
    start_time=time()
    if A is None or B is None:
        end_time=time()
        print(f"Total time taken by execution is {start_time-end_time}")
        return (-1,-1)
    if M<m or N<n:
        end_time=time()
        print(f"Total time taken by execution is {start_time-end_time}")
        return (-1,-1)
    answer =[]

    for i in range(0,M-m+1): 
        for j in range(N-n+1):
            found = True
            count=m*n
            unmatch=0
            
            
            if np.array_equal(A[i][j],B[0][0]):
            # if (A[i][j]==B[0][0]):
                for r in range(0,m): 
                    for s in range(0,n):
                        # if (B[r][s]!=A[r+i][s+j]):
                        
                        if np.array_equal(B[r][s],A[r+i][s+j])==False:
                             unmatch+=1
                             if unmatch>0.2*count:
                                 found = False
                                 break

                if found:
                    match=round((count-unmatch)/count*100,2)
                    answer.append((i,j,match))
                   
                    
    end_time=time()
    print(f"Toatal time taken is :{end_time-start_time}")
    return answer

print(SearchSubMatrix(a,b,1000,1000,2,2))    

