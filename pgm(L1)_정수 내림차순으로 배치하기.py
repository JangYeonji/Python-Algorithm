def solution(n):
    #1000000000 이상 자연수는 int로 바꿔줘야 함
    return int("".join(sorted(str(int(n)), reverse=True)))