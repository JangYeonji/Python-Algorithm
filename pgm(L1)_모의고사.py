from bisect import bisect_left
def solution(answers):
    answer = [0]*3
    result = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, i in enumerate(answers):
        if i == num1[idx%len(num1)]:
            answer[0] += 1
        if i == num2[idx%len(num2)]:
            answer[1] += 1
        if i == num3[idx%len(num3)]:
            print(i)
            answer[2] += 1
            
    for idx, i in enumerate(answer):
        if i==max(answer):
            result.append(idx+1)
    
    return result