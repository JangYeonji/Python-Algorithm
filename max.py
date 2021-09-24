#최댓값 구하기

### if문 이용
a = 123
b = 354
c = 103
maximum = a
if b > maximum :  
	maximum = b
if c > maximum:
  maximum = c
print ("최댓값은 {}".format(maximum))

### 함수, sorted 이용
def max_out(a, b, c):
    if type(a) == int and type(b) == int and type(c) == int: 
        return sorted([a, b, c])[-1]
    else: 
        return -1   #문자 입력되었을 때