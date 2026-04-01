class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Checking rows
        for row in range(9):
            mySet = set()
            for col in range(9):
                val = board[row][col]
                if val == '.': continue
                if val in mySet: return False
                mySet.add(val)

        #Checking columns
        for col in range(9):
            mySet = set()
            for row in range(9):
                val = board[row][col]
                if val == '.': continue
                if val in mySet: return False
                mySet.add(val)
        
        #Check all nine 3*3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                mySet = set()
                for r in range(3):
                    for c in range(3):
                        val = board[box_row * 3 + r][box_col * 3 + c]
                        if val == '.': continue
                        if val in mySet: return False
                        mySet.add(val)

        return True




         