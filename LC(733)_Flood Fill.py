class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        dx = [-1,0,1,0] 
        dy = [0,-1,0,1]
        
        q = []
        if image[sr][sc] != newColor:
            q = [(sr,sc)]
        point = image[sr][sc]
        image[sr][sc] = newColor
        
            
        while q:
            sr2,sc2 = q.pop(0)
            for i in range(4):
                nx = sr2 + dx[i]
                ny = sc2 + dy[i]
                if nx>=0 and nx<len(image) and ny>=0 and ny<len(image[0]):
                    if image[nx][ny]==point:
                        image[nx][ny] = newColor
                        q.append((nx,ny))
        
        return image