class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        cols = []
        boxes = []

        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        
        for r in range(9):

            for c in range(9):


                if board[r][c] == ".":
                    continue
                
                val = board[r][c]

                row_of_boxes = r // 3
                col_of_boxes = c // 3
                b = row_of_boxes * 3 + col_of_boxes

                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        
        return True
