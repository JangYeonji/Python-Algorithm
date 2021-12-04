#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, s):
        def fel(ss):
            half = len(ss)//2
            for i in range(half):
                if s[i] != s[-(i+1)]:
                    return False 
            return True
        tmp = ''
        leng = len(s)
        if fel(s)==False:
            for i in range(leng):
                tmp += s[i]
                s += tmp[::-1]
                if fel(s)==True:
                    break
                for i in range(len(tmp)):
                    s = s[:leng]
        return len(s)