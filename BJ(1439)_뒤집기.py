'''입력 예제
0001100

11111

00000001

1100110011001100001

11101101
'''

s = input()

change = [0]
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        change.append(i)
change.append(len(s))

zeros = []
ones = []

for i in range(len(change)-1):
    if s[change[i]] == '1':
        ones.append(s[change[i]:change[i + 1]])
    else:
        zeros.append(s[change[i]:change[i + 1]])

result = min(len(ones),len(zeros))
print(result)