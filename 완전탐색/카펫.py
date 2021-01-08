# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(brown, yellow):
    for i in range(yellow):
        height = i + 1

        if yellow % height == 0:
            width = yellow // height

            if width * 2 + height * 2 + 4 == brown:
                return [width + 2, height + 2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    brown = 10
    yellow = 2
    print(solution(brown, yellow))
