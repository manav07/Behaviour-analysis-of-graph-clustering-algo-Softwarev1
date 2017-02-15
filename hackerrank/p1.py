# Program to multiply two matrices using nested loops
import numpy as np
import xlrd
from builtins import str

def normalize(A):
    column_sums = A.sum(axis=0)
    new_matrix = A / column_sums[np.newaxis, :]
    return new_matrix


workbook = xlrd.open_workbook('1.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[0])

roww=0
coll=0
a=[]
for row_idx in range(sheet.nrows):
    #print(sheet.cell(row_idx,0))
    for col_idx in range(sheet.ncols):
        cell = sheet.cell(row_idx, col_idx)            
        print(str(int(cell.value))+"   ",end="")
        cell.value=int(cell.value)
        coll=col_idx
        a.append(((cell.value)))
    roww=row_idx

    print()
print()
print(str(roww) + " " + str(coll))
print(a)
print(max(a))
roww=max(a)
roww=int(roww)
print(roww)
coll=roww
arr=np.empty( (roww,roww) )
print(arr)
print()
print()
for i in range(roww):
    for j in range(coll):
        if(i==j):
            arr[i][j]=0
        else :
            arr[i][j]=0
np.dtype('int32')
print(arr)
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell(i,0).value,end='')
        print(sheet.cell(i,1).value)
        arr[(int(sheet.cell(i,0).value)-1)][(int(sheet.cell(i,1).value)-1)]=1
        print(arr[(int(sheet.cell(i,0).value)-1)][(int(sheet.cell(i,1).value)-1)])
        
print()
print("hui")
print()
print(arr)
input()
# result is 3x4
arr=normalize(arr)
 
result = np.zeros( (300,300) )
print(arr)
# iterate through rows of X
for i in range(len(arr)):
   # iterate through columns of Y
   for j in range(len(arr[0])):
       # iterate through rows of Y
       for k in range(len(arr)):
          # print("this is arr[i][k]"+str(arr[i][k]))
           #print("this is arr[k][j]"+str(arr[k][j]))
         
           result[i][j] += arr[i][k] * arr[k][j]
           
           #print("this is the result"+str(result[i][j]))
           
		   
for r in result:
	
   	print(r)
   	input()
   
   
   
   