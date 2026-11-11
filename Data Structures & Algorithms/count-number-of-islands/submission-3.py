class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid[0]) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()


        def bfs(r, c, visited):

            queue = deque([(r,c)])
            visited.add((r,c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while queue:
                row, col = queue.popleft()
                

                for dr, dc in directions:
                    new_row = dr + row
                    new_col = dc + col

                    if new_row < 0 or new_row >= rows:
                        continue
                    if new_col < 0 or new_col >= cols:
                        continue

                    if grid[new_row][new_col] == "1" and (new_row,new_col) not in visited:
                            visited.add((new_row,new_col))
                            queue.append([new_row,new_col])


        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c, visited)
                    islands += 1

        return islands 