class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        q = []
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    q.append((i,j))
                    answer += 1
                    grid[i][j] = "2"
                    while q:
                        x,y = q.pop()
                        for d in range(4):
                            nx = dx[d]+x
                            ny = dy[d]+y
                            if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[i]):
                                if grid[nx][ny]=="1":
                                    q.append((nx,ny))
                                    grid[nx][ny] = "2"
                                
        return answer