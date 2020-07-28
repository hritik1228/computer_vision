#program to copy the array of one element into another array

#Initialize array   
arr1 = [1, 2, 3, 4, 5]   
   
#Create another array arr2 with size of arr1  
arr2 = [None] * len(arr1)

for i in range(0,len(arr1)):
    arr2[i]=arr1[i]
    
#original array
print('original array')    
for i in range(0,len(arr1)):
    print(arr1[i],end='')
    
#copied array    
print('\ncopied array')
for j in range(0,len(arr2)):
    print(arr1[j],end='')
    

    
#Initialize array   
arr = [1, 2, 8, 3, 2, 2, 2, 5, 1]
#Array fr will store frequencies of element  
fr = [None] * len(arr)

visited = -1;  
   
for i in range(0, len(arr)):  
    count = 1;  
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            count = count + 1;  
            #To avoid counting same element again  
            fr[j] = visited;  
              
    if(fr[i] != visited):  
        fr[i] = count;  
   
#Displays the frequency of each element present in array  
print("---------------------");  
print(" Element | Frequency");  
print("---------------------");  
for i in range(0, len(fr)):  
    if(fr[i] != visited):  
        print("    " + str(arr[i]) + "    |    " + str(fr[i]));  
print("---------------------");  



#Program to left rotate the elements of an array
arr1=[1,2,3,4,5]
n=3

for i in range(0,len(arr1)):
    print(arr1[i],end=' ')
print('\n')
    
for i in range(0,n):
    first=arr1[0]
    for j in range(0,len(arr1)-1):
        arr1[j]=arr1[j+1]
        
arr1[len(arr1)-1] = first

for q in range(0,len(arr1)):
    print(arr1[q],end=' ')
    
#program to print the duplicate element in an array
    
arr=[1,2,1,2,3,2,6,2,1,9,7,3]
for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            print(arr[j],end=' ')

#Program to print the elements of an array in reverse order

arr=[1,2,3,4,5]
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print('\n')
for j in range(len(arr)-1,-1,-1):
    print(arr[j],end=' ')

#Program to print the elements of an array present on odd position
arr=[1,2,3,4,5]
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print('\n')

for j in range(0,len(arr),2):
    print(arr[j])

#Program to print the elements of an array present on even position
arr=[1,2,3,4,5]
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print('\n')

for j in range(1,len(arr),2):
    print(arr[j])


#Program to print the largest element present in an array



    







































