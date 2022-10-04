def solution(s):

    maax = -1e9
    miin = 1e9
    for i in s.split():
        if int(i) > maax:
            maax = int(i)
        if int(i) < miin:
            miin = int(i)

    return str(miin) + ' ' + str(maax)