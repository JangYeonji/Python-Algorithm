def solution(n, arr1, arr2):
    answer = []
    
    for x,y in zip(arr1,arr2):
        answer.append(bin(x|y))
    
    answer = [x.replace("0b","") for x in answer]
    answer = [x.zfill(n) for x in answer]
    answer = [x.replace("1","#") for x in answer]
    answer = [x.replace("0"," ") for x in answer]
    
    return answer