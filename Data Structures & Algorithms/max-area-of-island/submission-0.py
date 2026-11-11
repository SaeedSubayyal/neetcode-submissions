class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r,c,visited):

            area = 1
            queue = deque([(r,c)])
            visited.add((r,c))
            

            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while queue:

                row, col = queue.popleft()

                for dr, dc in directions:

                    newRow = row + dr
                    newCol = col + dc

                    if newRow < 0 or newRow >= rows:
                        continue
                    if newCol < 0 or  newCol >= cols:
                        continue

                    if grid[newRow][newCol] == 1 and (newRow,newCol) not in visited:

                        visited.add((newRow,newCol))
                        queue.append((newRow,newCol))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and (r,c) not in visited:
                    area_local = bfs(r,c,visited)
                    max_area = max(max_area, area_local)
                    
                
        return max_area
