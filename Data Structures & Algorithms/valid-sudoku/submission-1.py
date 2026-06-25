class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_freq = {}
        col_freq = {}
        box_freq = {}

        for row in range (len(board)):
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    row_freq[f"{board[row][col]}-{row}"] = row_freq.get(f"{board[row][col]}-{row}", 0) + 1
        
        if any([f > 1 for f in row_freq.values()]):
            return False

        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] != '.':
                    col_freq[f"{board[row][col]}-{col}"] = col_freq.get(f"{board[row][col]}-{col}", 0) + 1
           
        if any([f > 1 for f in col_freq.values()]):
            return False


        for box in range(len(board)):
            i  = 0
            while i < int(math.sqrt(len(board))):
                j = 0
                while j < int(math.sqrt(len(board[0]))):
                    _row = (box // 3) * 3 + i
                    _col = (box % 3) * 3 + j                    
                    if board[_row][_col] != '.':
                        box_freq[f"{box}-{board[_row][_col]}"] = box_freq.get(f"{box}-{board[_row][_col]}", 0) + 1
                    j += 1
                i+= 1
        
        if any([f > 1 for f in box_freq.values()]):
            return False
        return True
