n = int(input())
food = list(map(int,input().split()))

result = []
result.append(food[0])
result.append(max(food[0],food[1]))

for i in range(2,n):
    result.append(max(food[i-1],food[i-2]+food[i]))
    
print(result[-1])