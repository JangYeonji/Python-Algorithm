def solution(sizes):
    answer = 0
    w = 0
    h = 0
    
    for size in sizes:
        if size[0]>size[1]:
            if w<size[0]:
                w = size[0]
            if h<size[1]:
                h = size[1]
        else:
            if h<size[0]:
                h = size[0]
            if w<size[1]:
                w = size[1]
    return w*h