# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    return all(base != x[:len(base)] for idx, base in enumerate(phone_book) for x in phone_book[idx + 1:])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    phone_book = ["12", "123", "1235", "567", "88"]
    print(solution(phone_book))
