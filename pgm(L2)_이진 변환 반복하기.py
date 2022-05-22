def solution(s):
    answer = [0]*2
    while s!="1":
        answer[1] += s.count("0")
        answer[0] += 1
        s = str(bin(s.count("1"))).replace("0b","")
    return answer