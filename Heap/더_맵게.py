# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first + second * 2)
        answer += 1

    if scoville[0] >= K:
        return answer
    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))