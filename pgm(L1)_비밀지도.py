def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = arr1[i] | arr2[i]
        answer.append(str(bin(a)).replace("0b","").zfill(n).replace("1","#").replace("0"," "))

    return answer