class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                digit = board[r][c]

                if digit == ".":
                    continue

                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if (
                    digit in rows[r]
                    or digit in cols[c]
                    or digit in boxes[box]
                ):
                    return False

                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

        return True 