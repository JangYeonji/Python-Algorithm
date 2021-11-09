'''
123402

7755
'''

n = input()
half = int(len(n)/2)
ls=0;rs=0
for idx, i in enumerate(n):
    if idx<half:
        ls += int(i)
    else:
        rs += int(i)
if ls==rs:
    print('LUCKY')
else:
    print('READY')