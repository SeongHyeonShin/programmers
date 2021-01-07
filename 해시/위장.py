# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from collections import Counter


def solution(clothes):
    _dict = Counter(map(lambda x: x[1], clothes))

    num = 1
    for _key in _dict.keys():
        num *= _dict[_key] + 1

    return num - 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
