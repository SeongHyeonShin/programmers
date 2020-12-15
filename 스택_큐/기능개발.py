# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


def solution(progresses, speeds):
    ans = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while len(progresses):
        count = 0
        while len(progresses) and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count: ans.append(count)
        for idx in range(len(progresses)):
            progresses[idx] += speeds[idx]

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))
