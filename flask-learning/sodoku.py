result = ""

def solve(bo):
    bo = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"

    # try to solve the board
    # Check the input board have 81 len
    if bo != "" and len(bo) == 81:
        bo = split_board(bo)

        find = find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0

        return False
    return result

# break the board
def split_board(bo):
    newBoard = []
    newBoard.append(str(bo[0:9]))
    newBoard.append(str(bo[9:18]))
    newBoard.append(str(bo[18:27]))
    newBoard.append(str(bo[27:36]))
    newBoard.append(str(bo[36:45]))
    newBoard.append(str(bo[45:54]))
    newBoard.append(str(bo[54:63]))
    newBoard.append(str(bo[63:72]))
    newBoard.append(str(bo[72:81]))

    return newBoard


# find empty
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True
