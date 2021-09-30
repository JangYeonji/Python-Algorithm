#최대공약수와 최소공배수 (다시. 채점에서 오류남)
'''
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
'''

#mine
def solution(n, m):
    answer = []
    if n>m:
        n,m = m,n
        
    answer.append(n) if m%n==0 else answer.append(1)
    answer.append(m) if m%n==0 else answer.append(n*m)
    return answer


#ㄳ
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer