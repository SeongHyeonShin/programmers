# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solution(numbers):
    return str(int(''.join(map(str, sorted(numbers, key=lambda x: str(x) * 3, reverse=True)))))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [40, 403]
    print(solution(numbers))
