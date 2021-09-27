# 구구단

### 짝수단 출력, 3의 배수 제외
for x in range(2, 10):
    if x % 2 == 0 and x % 3 != 0 :
        for y in range(1, 10):
            print ("{} x {} = {}".format(x, y, x*y))

### 일반 구구단
[f"{x} x {y} = {x*y}" for x in range(2, 10) for y in range(1, 10)]