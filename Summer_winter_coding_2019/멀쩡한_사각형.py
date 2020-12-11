# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import gcd


def solution(w, h):
    return w * h - (w + h - gcd(w, h))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w = 8
    h = 12
    print(solution(w, h))
