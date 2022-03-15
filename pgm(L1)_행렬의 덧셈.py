def solution(arr1, arr2):
    one = len(arr1)
    two = len(arr1[0])
    
    #[0]*n 오류남
    answer = [[0 for i in range(two)] for i in range(one)]
        
    for i in range(one):
        for j in range(two):
            answer[i][j] = arr1[i][j]+arr2[i][j]
    
    return answer