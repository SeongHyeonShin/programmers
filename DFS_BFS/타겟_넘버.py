# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

answer = 0


def dfs(numbers, target, total, i):
    global answer
    if len(numbers) == i:
        if target == total: answer += 1
        return

    dfs(numbers, target, total + numbers[i], i + 1)
    dfs(numbers, target, total - numbers[i], i + 1)


def solution(numbers, target):
    global answer
    dfs(numbers, target, numbers[0], 1)
    dfs(numbers, target, -numbers[0], 1)

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
