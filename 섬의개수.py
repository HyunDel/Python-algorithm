from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            # 육지가 아닐때 종료
            if i < 0 or i>=len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            
            grid[i][j]=0 
            # 동서남북으로 재귀
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        count = 0
        # 육지일때 탐색하기
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count +=1
        return count