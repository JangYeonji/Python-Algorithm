#211126
#### 1차 시도. 정확성 1,2,3,4,7,18,25,27,29,30,31,32 빼고 실패
'''
food_times = [3,1,2]
k=5 #1
food_times = [1,100]
k=5 #2
food_times = [4,2,3,6,7,1,5,8]
k=16 #3
food_times = [4,2,3,6,7,1,5,8]
k=27 #5
food_times = [1,1,1,1]
k=7 #-1
food_times = [3,1,1,1,2,4,3] -> 실패
k=12 #6
food_time = [4,3,5,6,2]
k=7 #3
food_time = [4,1,1,5]
k=4 #1
'''

def solution(food_times, k):
    idx = []
    for i in range(len(food_times)):
        idx.append(i)
    x = 0
    limit = len(idx)
    for i in range(k):
        if food_times[idx[x]]>0:
            food_times[idx[x]] -= 1
        x += 1
        if x>=limit:
            x = 0
        if food_times[idx[x]]==0:
            idx.remove(idx[x])
            limit -= 1
        if limit==0:
            break
    if food_times.count(0)==len(food_times):
        return -1
    else:
        return idx[x]+1