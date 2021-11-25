'''입력 예시
5
'''

n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(n) in str(h) or str(n) in str(m) or str(n) in str(s):
                count += 1
print(count)