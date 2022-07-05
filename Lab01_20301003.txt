#Task_01

def shiftLeft(source,k):

    for i in range(0,k):
        source[i] = source[i+k]
    for i in range(k,len(source)):
        source[i]=0


source=[ 10,20,30,40,50,60 ]
shiftLeft(source,3)
print(source)


#Task_02

def rotateLeft(source,k):
    
    temp_src = [0]*6

    for i in range(0,k):
        temp_src[i]= source[i]
        #print(temp_src)

    for i in range(0,k):
        source[i] = source[i+k]
        #print(temp_src)

    for i in range(0,k):
        source[i+k]= temp_src[i]


source=[10,20,30,40,50,60]
rotateLeft(source,3)
print(source)


#Task_03

def shiftRight(source,k):

    for i in range(0,k):
        source[i+k] = source[i]
    for i in range(0,k):
        source[i]=0


source=[ 10,20,30,40,50,60 ]
shiftRight(source,3)
print(source)


#Task_04

def rotateLeft(source,k):
    
    temp_src = [0]*6

    for i in range(0,k):
        temp_src[i]= source[i]
        #print(temp_src)

    for i in range(0,k):
        source[i] = source[i+k]
        #print(temp_src)

    for i in range(0,k):
        source[i+k]= temp_src[i]


source=[10,20,30,40,50,60]
rotateLeft(source,3)
print(source)


#Task_05

def remove(source,size,idx):
    

    for i in range(idx,size):
        source[i]= source[i+1]
        
source=[10,20,30,40,50,0,0]
remove(source,5,2)
print(source)

# task_06

def removeAll(source, size, element):
    arr = [0] * size
    j = 0
    for i in range(size):
        if source[i] != 2:
            arr[j] = source[i]
            j += 1

    return arr


source = [10,2,30,2,50,2,2,0,0]
print(removeAll(source,7,2))


#Task_07

def solve(arr):
    i = len(arr) // 2
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for p in range(0, i + 1):
        sum1 = sum1 + arr[p]
    for q in range(i + 1, len(arr)):
        sum2 = sum2 + arr[q]

    for m in range(0, i):
        sum3 += arr[m]
    for n in range(i, len(arr)):
        sum4 += arr[n]

    if (sum1 == sum2 or sum3 == sum4):
        print('true')
    else:
        print('false')


a = [2, 1, 1, 2, 1]
print(solve(a))



#Task_08

def ArraySeries(num):
    
    for i in range(num,0,-1):
        for j in range(num,0,-1):
            z=num-i+1
            if j<=z:
                print(j)
            else:
                print(0)

ArraySeries(4)


#Task_09

def bunch(arr):
    res = 1
    maxi = 0

    for i in range(0, len(arr)-1):
        if arr[i + 1] == arr[i]:
            res += 1
            if res > maxi:
                maxi = res
        else:
            res = 1

    print(maxi)

b =  [1, 2, 2, 3, 4, 4, 4] 
bunch(b)

#Task_10



{3,4,6,3,4,7,4,6,8,6,6}


