#사용자 함수

def pal_check(text):
    return text == text[::-1]
pal_check("rotavator")   #True

def temp(a=10, b=20):
    return a + b
temp(b=35)   #45