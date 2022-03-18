def solution(board, moves):
    answer = []
    result = 0
    
    for m in moves:
        for b in board:
            if b[m-1]!=0:
                answer.append(b[m-1])
                b[m-1]=0
                break
        if len(answer)>=2 and answer[-1]==answer[-2]:
            answer.pop()
            answer.pop()
            result += 2
    
    return result