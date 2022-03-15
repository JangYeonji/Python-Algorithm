def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i==answer[-1]:
            continue
        else:
            answer.append(i)
    return answer