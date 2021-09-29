#행렬의 덧셈 (다시)
'''
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
'''

#mine -> 런타임에러
def solution(arr1, arr2):
    answer = [[]]
    answer = [[0]*len(arr1[0]),[0]*len(arr1[1])]
    
    for i in range(len(arr1)):
        for j in range(len(arr1[1])):
            answer[i][j] = arr1[i][j]+arr2[i][j]
    return answer

#ㄳ
def sumMatrix(A,B):
            #[[1,2],[3,4]], [[3,4],[5,6]]
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
                                            #   a        b
                                            #[[1,2],   [3,4]]
                                            #[[3,4],   [5,6]]
                    #   c,d    c,d
                    #[[(1,3), (2,4)], 
                    # [(2,5), (4,6)]]

    return answer