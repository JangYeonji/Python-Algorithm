#대소문자 구분없이 동명이인 찾기

name = ['Tom', "Jerry", "MikE", "Tom", "Mike", "tom", "tOm"]

### for문
def search_list(name):
    result = set()
    n = len(name)
    name = [x.lower() for x in name]
    for i in range(0, n-1):
        for j in range(i+1, n):
            print ("{} == {}".format(name[i], name[j]))
            if name[i] == name[j]:
                result.add(name[i])
    return list(result)

search_list(name)


### while문
def search_while(name):
    result = set()
    n = len(name)
    name = [x.lower() for x in name]
    i = 0
    while i <= n-1:
        j = i + 1
        while j < n:
            if name[i] == name[j]:
                result.add(name[i])
            j += 1
        i += 1
    return list(result)

search_while(name)