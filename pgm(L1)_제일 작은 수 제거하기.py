def solution(arr):
    m = min(arr)
    arr.remove(m)
    if arr != []:
        return arr
    else:
        return [-1]