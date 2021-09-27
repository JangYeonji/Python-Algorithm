#최댓값 위치 구하기

a = [123,52,4,4,6,35,234244, 524,266, 8888888,23424,2424, 8888888,23,4]

def search_index(data):
		### 방법1
    n = len(data)
    max_idx = 0
    for x in range(1, n):
        if data[x] > data[max_idx]:
            max_idx = x
    return max_idx

		### 방법2
    return data.index(max(data))

search_index(a)