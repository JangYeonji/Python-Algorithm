'''입력 예시
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
'''

n = int(input())
council = []
for i in range(n):
    council.append(list(map(int,input().split())))

maxx = 0

for jdx in range(n):
    idx = 0
    money = 0
    while idx < len(council[jdx:]):
        if council[idx][0]+idx > len(council[jdx:]):
            break
        money += council[idx][1]
        idx += council[idx][0]
    if maxx < money:
        maxx = money

print(maxx)

