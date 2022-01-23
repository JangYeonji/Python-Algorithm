class Solution:
    def reverseBits(self, n: int) -> int:
        
        a = str(bin(n)).replace('0b','').zfill(32)
        answer = 0
        for idx, i in enumerate(a):
            if i!='0':
                answer += 2**idx
        
        return answer