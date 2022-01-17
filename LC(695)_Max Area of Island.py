class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        tmp = 0
        answer = 0
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    tmp += 1
                    q = [(x,y)]
                    while q:
                        xpop, ypop = q.pop(0)
                        for d in range(4):
                            nx = xpop+dx[d]
                            ny = ypop+dy[d]
                            if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny]==1:
                                grid[nx][ny] = 2
                                tmp += 1
                                q.append((nx,ny))
                if tmp>answer:
                    answer = tmp
                tmp = 0
        
        return answer