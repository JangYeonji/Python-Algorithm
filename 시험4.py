#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, price, cost):
        answer = [0]*len(price)
        for idx,i in enumerate(price):
            for jdx,j in enumerate(cost):
                if i>j and i<=price[jdx]:
                    answer[idx] += i-j
        
        if max(answer)==0:
            return 0
            
        index = []
        result = int(1e9)
        for idx,i in enumerate(answer):
            if i==max(answer):
                index.append(idx)
        for i in index:
            if result>price[i]:
                result = price[i]
        return result