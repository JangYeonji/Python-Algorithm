'''
- 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
- 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
'''

#mine
#2차시도 -> 2,4,10,11,12 실패
#2,10,11,12는 제곱수 포함 안해서?

def solution(n):
    answer = 0
    num = []
    
    for i in range(1,len(n)+1):
        num.append(n[i-1])
        for a in range(0,len(n)-1):
            num.append(n[i-1] + n[(len(n)+i+a) % len(n)])

        for b in range(1,len(n)-1):
            num.append(n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+b) % len(n)])
            num.append(n[i-1] + n[(len(n)+i+b) % len(n)] + n[(len(n)+i) % len(n)])
            num.append(n[(len(n)+i+b) % len(n)] + n[(len(n)+i) % len(n)] + n[i-1])

        for c in range(2,len(n)-1):
            num.append(n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+c)%len(n)])
            num.append(n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+c)%len(n)] + n[i-1])
            num.append(n[(len(n)+i+1) % len(n)] + n[(len(n)+i+c)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)])
            num.append(n[(len(n)+i+c)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)])

        for d in range(3,len(n)-1):
            num.append(n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+d)%len(n)])
            num.append(n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+d)%len(n)] + n[i-1])
            num.append(n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+d)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)])
            num.append(n[(len(n)+i+2)%len(n)] + n[(len(n)+i+d)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)])
            num.append(n[(len(n)+i+d)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)])

        for e in range(4,len(n)-1):
            num.append(n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+3)%len(n)] + n[(len(n)+i+e)%len(n)])
            num.append(n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+3)%len(n)] + n[(len(n)+i+e)%len(n)] + n[i-1])
            num.append(n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+3)%len(n)] + n[(len(n)+i+e)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)])
            num.append(n[(len(n)+i+2)%len(n)] + n[(len(n)+i+3)%len(n)] + n[(len(n)+i+e)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)])
            num.append(n[(len(n)+i+3)%len(n)] + n[(len(n)+i+e)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)])
            num.append(n[(len(n)+i+e)%len(n)] + n[i-1] + n[(len(n)+i) % len(n)] +  n[(len(n)+i+1) % len(n)] + n[(len(n)+i+2)%len(n)] + n[(len(n)+i+3)%len(n)])
                         
    for cnt in list(set(map(int,num))):
        bool_prime = True
        prime = int(cnt ** (1/2))
        if cnt<=1:
            bool_prime = False
        else:
            for i in range(2,prime):
                if cnt%i==0:
                    bool_prime = False
        if bool_prime==True:
            answer+=1
            
    return answer

#ㄳ
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
				# list(n) : '17' -> ['1', '7']
				# set(map("".join, permutations(list(n), i+1))) : list(n)을 1개, 2개씩 조합 -> {'1', '7'}, {'71', '17'}
				# set(map(int, map("".join, permutations(list(n), i + 1)))) : int로 변경 -> {1, 7}, {17, 71}
				# a |= set(map(int, map("".join, permutations(list(n), i + 1)))) : 비트로 or 연산 -> {1, 7, 17, 71}
    
		a -= set(range(0, 2))   #a에서 0,1 빼기
    for i in range(2, int(max(a) ** 0.5) + 1):   #2부터 최댓값의 루트값까지
        a -= set(range(i*2, max(a)+1, i))   #소수가 아닌 값 제거
    return len(a)