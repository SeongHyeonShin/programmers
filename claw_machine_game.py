# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


"""
# best
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
"""


# my code
def solution(board, moves):
    uncount = 0
    pointer = [0] * len(board)
    dq = deque()

    for i in range(len(board)):
        while board[pointer[i]][i] == 0 and pointer[i] < len(board):
            pointer[i] += 1

    for m in moves:
        if pointer[m-1] < len(board) and board[pointer[m-1]][m-1] != 0:
            dq.pop() if len(dq) and dq[-1] == board[pointer[m-1]][m-1] else dq.append(board[pointer[m-1]][m-1])
            pointer[m-1] += 1
        else:
            uncount += 1

    return len(moves) - len(dq) - uncount


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))