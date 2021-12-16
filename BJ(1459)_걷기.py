'''입력예제
4 2 3 10
4 2 3 5
2 0 12 10
25 18 7 11
24 16 12 10
10000000 50000000 800 901
135 122 43 29
'''

x,y,w,s = map(int,input().split())

if (w*2)<s:
    print((x+y)*w)
else:
    if abs(x-y)%2==0:
        print((s*min(x,y))+min(w,s)*abs(x-y))
    else:
        print((s*min(x,y))+(min(w,s)*(abs(x-y)-1)+w))