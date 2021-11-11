#ㄳ1
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

#ㄳ2
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])

#ㄳ3
def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i,j)] = x

    return x