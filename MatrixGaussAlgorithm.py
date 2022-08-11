import numpy as np

m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = np.zeros((m,n), dtype=int)
u = len(a)

for k in range(u):
    for h in range(len(a[k])):
        x = int(input("Enter Element: "))
        a[k][h] = x
arr = np.array(a)
j = 0
currdim = 0
while j < n-1:
    for i in range(m):
        if arr[i,j] != 0:
            pivot = i 
            break 
    temp = arr[currdim,:].copy()
    arr[currdim,:] = arr[pivot,:]
    arr[pivot,:] = temp
    if arr[currdim,j] != 0: 
        arr[currdim,:] = np.multiply(arr[currdim,:], 1/arr[currdim,j]).copy()
    else:
        continue
    for i in range(currdim + 1,m):
        if arr[i,j] != 0:
            arr[i,:] = np.add(arr[i,:], arr[currdim,:]*(-arr[i,j])).copy()
                   
    currdim+=1 
    j+=1 

print(arr)










  






    

        


                


    

        





















        