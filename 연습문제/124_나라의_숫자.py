# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(n):
    answer = ''
    table = ['4', '1', '2']

    while n > 0:
        answer += table[int(n % 3)]
        n = (n - 1) // 3

    return "".join(reversed(answer))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 10
    print(solution(n))
