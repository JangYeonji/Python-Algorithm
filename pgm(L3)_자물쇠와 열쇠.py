#상하좌우 이동 못함
def turn(key):
    n = len(key)
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = key[i][j]
    return tmp
def one(key):
    kxy = []
    for idx, i in enumerate(key):
        for jdx, j in enumerate(i):
            if j==1:
                kxy.append((idx,jdx))
    return kxy
def find(lxy,kxy):
    a = ''
    for i in lxy:
        if i in kxy:
            a += '1'
        else:
            a += '0'
    return a

def solution(key, lock):
    lxy = []
    answer = False
    for idx, i in enumerate(lock):
        for jdx, j in enumerate(i):
            if j==0:
                lxy.append((idx,jdx))
    for i in range(4):
        kxy = one(key)
        a = find(lxy,kxy)
        if '0' not in a:
            break
            answer = True
        else:
            key = turn(key)
    return answer