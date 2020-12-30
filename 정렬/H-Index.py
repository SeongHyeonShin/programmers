# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solution(citations):
    return sum(1 for i, v in enumerate(sorted(citations, reverse=True)) if v >= i + 1)

    # 다른 풀이
    # return max(map(min, enumerate(sorted(citations, reverse=True), start=1)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))
