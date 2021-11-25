'''입력 예시
a1
'''

night = input()
count = 0
steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
for i in steps:
    nx = ord(night[0]) + i[0]
    ny = int(night[1]) + i[1]
    if nx<ord('a') or nx>ord('z') or ny<1 or ny>8:
        continue
    else:
        count += 1