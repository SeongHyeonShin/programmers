# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(s):
    ans = len(s)

    for i in range(1, len(s) // 2 + 1):
        count = 0
        length = 0
        for j in range(i, len(s) + i, i):
            if s[j-i:j] == s[j:j+i]:
                count += 1
            else:
                if count:
                    length += len(str(count + 1))
                length += len(s[j-i:j])
                count = 0

        ans = min(ans, length)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    print(solution(s))
