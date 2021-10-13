#1차시도 : 2,3,4,5,6,7,8,9,10 & 효율성테스트 실패

def solution(prices):
    stack = [0]   
    answer = [0] * len(prices)
    
    for i in range(1,len(prices)):
        if prices[i] < prices[stack[-1]]:  
            for j in stack[::-1]:   
                if prices[i] < prices[j]:   
                    answer[j] = 1  
                    stack.pop()
        stack.append(i)

    for i in stack:  
        answer[i] = len(prices) - (i+1)
    return answer

#prices = [1,2,3,2,3,1], answer = [5,4,1,2,1,0] 으로 고쳐서 해보기