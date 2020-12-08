# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from itertools import combinations


def solution(numbers):
    return sorted(set([sum(comb) for comb in combinations(numbers, 2)]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [5,0,2,7]
    print(solution(numbers))
