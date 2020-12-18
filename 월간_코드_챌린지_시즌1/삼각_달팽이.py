# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(n):
    result = [[0] * (i + 1) for i in range(n)]
    x, y = -1, 0
    shift = [[1, 0], [0, 1], [-1, -1]]
    count = 1

    for i in range(n):
        for _ in range(n - i):
            s = shift[i % 3]
            x += s[0]
            y += s[1]

            result[x][y] = count
            count += 1

    return [v for row in result for v in row]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 5
    print(solution(n))
