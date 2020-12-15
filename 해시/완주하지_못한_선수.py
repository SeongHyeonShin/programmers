# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter


def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution(participant, completion))
