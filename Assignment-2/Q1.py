#!/usr/bin/python
# Kaustav Vats (2016048)

from time import time

class Board:

    def __init__(self, size, board):
        self.size = size
        if board == None:
            self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        else:
            mat = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            for i in range(self.size):
                for j in range(self.size):
                    mat[i][j] = board[i][j]           
            self.board = mat

    def __repr__(self):
        return "Board()"

    def __str__(self):
        print("\n")
        for i in range(self.size):
            for j in range(self.size):
                if ( j == 2 ):
                    print(self.board[i][j], end=' ')
                else:
                    print(self.board[i][j], end=' | ')
            print("\n")
        print()

    def printMatrix(self):
        print("\n")
        for i in range(self.size):
            for j in range(self.size):
                if ( j == 2 ):
                    print(self.board[i][j], end=' ')
                else:
                    print(self.board[i][j], end=' | ')
            print("\n")
        print()

    def isMoveLeft(self):
        for i in range(self.size):
            for j in range(self.size):
                if ( self.board[i][j] == '_' ):
                    return True
        return False

    def evaluate(self, user, computer):
        for i in range(self.size):
            if ( self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] ):
                if ( self.board[i][0] == computer ):
                    return 1
                elif ( self.board[i][0] == user ):
                    return -1
        for i in range(self.size):
            if ( self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] ):
                if ( self.board[0][i] == computer ):
                    return 1
                elif ( self.board[0][i] == user ):
                    return -1
        # Diagonals
        if ( self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] ):
            if ( self.board[0][0] == computer ):
                return 1
            elif ( self.board[0][0] == user ):
                return -1
        if ( self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] ):
            if ( self.board[0][2] == computer ):
                return 1
            elif ( self.board[0][2] == user ):
                return -1
        return 0

class TicTacToe:
    # count1 = 0
    # count2 = 0

    def __init__(self, size, user, computer):
        self.size = size
        self.user = user
        self.computer = computer
        self.count1 = 0
        self.count2 = 0


    def MiniMax(self, board, isComputer):
        self.count1 = self.count1 + 1
        score = board.evaluate(self.user, self.computer)
        if ( score == 1 or score == -1 ):
            return score
        if ( not board.isMoveLeft() ):
            return 0
        if ( isComputer ):
            best = -10
            for i in range(self.size):
                for j in range(self.size):
                    if ( board.board[i][j] == '_' ):
                        board.board[i][j] = self.computer
                        best = max(best, self.MiniMax(board, not isComputer))
                        board.board[i][j] = '_'
            return best
        else:
            best = 10
            for i in range(self.size):
                for j in range(self.size):
                    if ( board.board[i][j] == '_' ):
                        board.board[i][j] = self.user
                        best = min(best, self.MiniMax(board, not isComputer))
                        board.board[i][j] = '_'
            return best

    def NextMove(self, board):
        BestValue = -10
        Matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        for i in range(self.size):
            for j in range(self.size):
                if ( board.board[i][j] == '_' ):
                    board.board[i][j] = self.computer
                    value = self.MiniMax(board, False)
                    # print("value:",value)
                    if ( value > BestValue ):
                        MatrixObject = Board(self.size, board.board)
                        Matrix = MatrixObject.board
                        BestValue = value

                    board.board[i][j] = '_'
        return MatrixObject

    def AlphaBetaPruning(self, board, aplha, beta, isComputer):
        self.count2 += 1
        score = board.evaluate(self.user, self.computer)
        if ( score == 1 or score == -1 ):
            return score
        if ( not board.isMoveLeft() ):
            return 0
        if ( isComputer ):
            best = -10
            for i in range(self.size):
                for j in range(self.size):
                    if ( board.board[i][j] == '_' ):
                        board.board[i][j] = self.computer
                        best = max(best, self.AlphaBetaPruning(board, alpha, beta, not isComputer))
                        board.board[i][j] = '_'
                        aplha = max(aplha, best)

                        if ( beta <= alpha ):
                            break
            return best
        else:
            best = 10
            for i in range(self.size):
                for j in range(self.size):
                    if ( board.board[i][j] == '_' ):
                        board.board[i][j] = self.user
                        best = min(best, self.AlphaBetaPruning(board, alpha, beta, not isComputer))
                        board.board[i][j] = '_'
                        beta = min(beta, best)

                        if ( beta <= alpha ):
                            break
            return best
    
    def NextMoveAplhaBeta(self, board, alpha, beta):
        BestValue = -10
        Matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        for i in range(self.size):
            for j in range(self.size):
                if ( board.board[i][j] == '_' ):
                    board.board[i][j] = self.computer
                    value = self.AlphaBetaPruning(board, alpha, beta, False)

                    if ( value > BestValue ):
                        MatrixObject = Board(self.size, board.board)
                        Matrix = MatrixObject.board
                        BestValue = value

                    board.board[i][j] = '_'
        return MatrixObject


if __name__ == "__main__":
    
    print("\n\tTic-Tac-Toe Game")
    print("\tPlayer vs Computer\n")
    user = 'X'
    computer = 'O'
    alpha = -10
    beta = 10

    while(True):
        print("\n\n\tSelect Algorithm:-")
        print("\t1. MiniMax")
        print("\t2. AlphaBetaPruning")
        print("\t3. Exit")
        algo = int(input(": "))
        if ( algo >= 3 ):
            break

        Matrix = Board(3, None)
        ttt = TicTacToe(3, user, computer)
        turn = True

        # PlayerMovesTesting = [[0,0], [2, 2], [2, 1], [1, 0]]
        # val = 0
        t1 = int(round(time()*1000))
        for i in range(9):
            if ( turn ):
                while(True):
                    print("Player's turn...")
                    x = int(input("x: "))
                    # x=0
                    y = int(input("y: "))
                    # y=0
                    # x = PlayerMovesTesting[val][0]
                    # y = PlayerMovesTesting[val][1]
                    # val += 1
                    if ( Matrix.board[x][y] != '_' ):
                        print("\tWrong Move!\n")
                        continue
                    Matrix.board[x][y] = user
                    # print(Matrix)
                    Matrix.printMatrix()
                    turn = False
                    break
            else:
                print("Computer's Turn")
                if ( algo == 1 ):
                    Matrix = ttt.NextMove(Matrix)
                    # print(Matrix)
                    Matrix.printMatrix()
                    turn = True
                elif ( algo == 2 ):
                    Matrix = ttt.NextMoveAplhaBeta(Matrix, alpha, beta)
                    Matrix.printMatrix()
                    turn = True

            output = Matrix.evaluate(user, computer)
            if ( output == -1 ):
                print("\nPlayer Wins!")
                break
            elif ( output == 1 ):
                print("\nComputer Wins!")
                break
            elif ( not Matrix.isMoveLeft() ):
                print("\nMatch Draw!")
                break
        t2 = int(round(time()*1000))
        print("Total time taken: ", t2-t1)  
        # print("Moves: ", ttt.count1, ttt.count2)

