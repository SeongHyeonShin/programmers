# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(people, limit):
    answer = len(people)
    p = sorted(people, reverse=True)
    s, e = 0, len(p) - 1

    while s < e:
        if p[s] + p[e] <= limit:
            e -= 1
            answer -= 1
        s += 1

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    people = 	[70, 80, 50]
    limit = 100
    print(solution(people, limit))
