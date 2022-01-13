class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ''
        for i in s.split():
            answer += (i[::-1] + ' ')
        return answer[:-1]