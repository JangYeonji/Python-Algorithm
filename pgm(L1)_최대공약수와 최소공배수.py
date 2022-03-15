def gcd(a,b):
    while a!=0:
        t = b%a
        (b,a) = (a,t)
    return b
def solution(n, m):
    answer = []
    if m<n:
        n,m = m,n
    g = gcd(n,m)
    answer.append(g)
    answer.append((n*m)/g)
    
    return answer