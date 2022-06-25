n = int(input())

array = [0] * (1001)    #for문, n+1 안 됨
array[1] = 1
array[2] = 2

for i in range(3,1001):    #n+1 안 됨
    array[i] = array[i-1]+array[i-2]
    
print(array[n]%10007)