'''
5
R R R U D D
'''

n = int(input())
map = input()
map = map.replace(" ","")

def trip(map,x,y):
    for i in map:
        if x<=0:
            x += 1
        elif y<=0:
            y += 1
        if i=='R':
            y += 1
        elif i=='L':
            y -= 1
        elif i=='U':
            x -= 1
        elif i=='D':
            x += 1
    return x,y

print(trip(map,1,1))