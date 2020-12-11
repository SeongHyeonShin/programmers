# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
# best code

from difflib import SequenceMatcher


def solution(s):
    return SequenceMatcher(None, s, s[::-1]).find_longest_match(0, len(s), 0, len(s)).size
"""


def isPalindrome(s):
    return all(s[i] == s[-1 - i] for i in range(len(s) // 2))


def solution(s):
    if len(s) == 1:
        return 1

    for i in range(1, len(s)):
        for j in range(i):
            if isPalindrome(s[j:len(s) - i + 1 + j]):
                return len(s) - i + 1

    return 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "a"
    print(solution(s))
