#다음에 다시 도전!

def solution(p):
    ans = [0] * len(p)   #배열 개수 지정
    stack = [0]   #주식 가격이 떨어지는 지점을 못찾은 가격의 index 모음

    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:     # 미래값++ < 현재값++
            for j in stack[::-1]:       
                if p[i] < p[j]:             # 미래값 < 현재값-- 
                    ans[j] = i-j                # 가격이 떨어진 시간 = 미래 시간 - 현재 시간
                    stack.pop()                 # 맨 위의 값(가격이 떨어진 시간) 삭제
                else:                       # 미래값 > 현재값이면 
                    break
        stack.append(i)   #1,2,3...초 후
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1   #스택 시간 = 최종 시간 - 스택에 저장된 시간 - 1
    return ans