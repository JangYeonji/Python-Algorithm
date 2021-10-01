#주식가격 (다시)
'''
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
'''
def solution(prices):
    timer = [0] * len(prices)   #배열 개수 지정
    stack = [0]   #주식값이 끝까지 안떨어진 주식값의 index들

    for i in range(1, len(prices)):
        if prices[i] < prices[stack[-1]]:   # 1<0, 2<1, 3<2... 값 비교.   현재값이 더 큰 경우(1초 뒤에 가격이 떨어짐)
            for j in stack[::-1]:               
                if prices[i] < prices[j]:           # 값이 떨어졌을 때보다 이전 값이 더 큰 경우 ([1,3,3,2,3]이면 2가 3,3들을 걸러냄)
                    stack.pop()                         # 맨 위의 값(가격이 떨어진 시간) 삭제
                    timer[j] = i-j                      # 가격이 떨어진 시간 = 값이 떨어진 시간(prices) - 값이 떨어질 시간(stack)
                else:                               # ([1,3,3,2,3]이면 2가 1을 만났을 때)                              
                    break                               # 스택 for문 빠져나감
        stack.append(i)   #[1,2,3]...초 후

    for i in range(0, len(stack)-1):
        timer[stack[i]] = len(prices) - stack[i] - 1   #스택 시간 = 총 시간 - 스택에 저장된 시간 - 1

    return timer