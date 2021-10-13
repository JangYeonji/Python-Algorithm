#2차시도 : 성공

def solution(prices):
    stack = [0]   
    answer = [0] * len(prices)
    
    for i in range(1,len(prices)):
        if prices[i] < prices[stack[-1]]:   
            for j in stack[::-1]:   
                if prices[i] < prices[j]:   
                    answer[j] = i-j 
                    stack.pop()
        stack.append(i)

    for i in stack: 
        answer[i] = len(prices) - (i+1)
    return answer