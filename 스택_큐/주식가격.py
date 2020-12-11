# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
from collections import deque


def solution(prices):
    prices = deque(prices)
    ans = []
    while len(prices):
        count = 0
        p = prices.popleft()
        for price in prices:
            count += 1
            if p > price: break

        ans.append(count)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices = [1,2,3,2,3]
    print(solution(prices))