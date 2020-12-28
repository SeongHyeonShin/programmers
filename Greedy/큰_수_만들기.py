# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


def solution(number, k):
    answer = deque(number[0])

    for num in number[1:]:
        while len(answer) and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)

    # deque는 slice 기능 지원 X
    if k: answer = list(answer)[:-k]
    return "".join(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = '1924'
    k = 2
    print(solution(number, k))
