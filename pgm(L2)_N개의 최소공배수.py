def solution(arr):
    answer = 0
    maax = max(arr)
    idx = 2
    
    while True:
        end = 0
        for a in arr:
            if maax % a != 0:
                maax = max(arr)*idx
                idx += 1
            else:
                end += 1
        if end==len(arr):
            break
    return maax