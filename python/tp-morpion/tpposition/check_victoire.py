board = [
    ["X", "X", "O"],
    [".", "X", "X"],
    [".", ".", "."]
]
for motif in ["XXX","OOO"]:
    ligne1 = board[0][0] + board[0][1] + board[0][2]
    ligne2 = board[1][0] + board[1][1] + board[1][2]
    ligne3 = board[2][0] + board[2][1] + board[2][2]
    col1 = board[0][0] + board[1][0] + board[2][0]
    col2 = board[0][1] + board[1][1] + board[2][1]
    col3 = board[0][2] + board[1][2] + board[2][2]
    diag1 = board[0][0] + board[1][1] + board[2][2]
    diag2 = board[0][2] + board[1][1] + board[2][0]
    if (ligne1 == motif or ligne2 == motif or ligne3 == motif
        or col1 == motif or col2 == motif or col3== motif
        or diag1 == motif or diag2 == motif):
        print("WIN")