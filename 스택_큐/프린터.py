# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


def solution(priorities, location):
    sorted_pr = deque(sorted(priorities, reverse=True))
    data = deque([[priorities[i], 1] if i == location else [priorities[i], 0] for i in range(len(priorities))])
    length = len(sorted_pr)

    while len(priorities):
        tmp_d = data.popleft()

        if not tmp_d[1]:
            sorted_pr.popleft() if tmp_d[0] == sorted_pr[0] else data.append(tmp_d)
        else:
            if tmp_d[0] == sorted_pr[0]: return length - len(sorted_pr) + 1
            else: data.append(tmp_d)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
