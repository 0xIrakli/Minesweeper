
class Solver:    
    def __init__(self, board, bomb_count):
        self.board = board
        self.w = len(board[0])
        self.h = len(board)
        self.count = bomb_count

    def solve(self):
        pass