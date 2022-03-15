def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = set()
        a = 1
        b = i
        while a<=b:
            if i%a==0:
                b = i/a
                count.add(a)
                count.add(b)
            a += 1
        if len(count)%2==0:
            answer += i
        else:
            answer -= i
    return answer