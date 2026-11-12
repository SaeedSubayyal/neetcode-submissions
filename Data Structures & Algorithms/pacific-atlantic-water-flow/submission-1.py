class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        result = []

        def dfs(r, c, visited):

            stack = [(r,c)]
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            visited.add((r,c))

            while stack:

                row, col = stack.pop()
                
                for dr, dc in directions:

                    newRow = dr + row 
                    newCol = dc + col

                    if newRow < 0 or newRow >= rows:
                        continue
                    if newCol < 0 or newCol >= cols:
                        continue
                    
                    if heights[newRow][newCol] < heights[row][col]:
                        continue

                    if (newRow,newCol) in visited:
                        continue
                    
                    stack.append((newRow,newCol))
                    visited.add((newRow,newCol))



        for r in range(rows):

            dfs(r,0, pacific)
            
            dfs(r,cols-1, atlantic)


        for c in range(cols):

            dfs(0,c,pacific)

            dfs(rows-1,c, atlantic)

        for (r,c) in pacific & atlantic:
            result.append([r,c])

        return result 
