# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# TEST CASE 통과
# 추가 TEST CASE에서 오답 존재
# e.g. "BBBBAAAAB"의 정답은 10, 아래 코드는 12를 출력

def solution(name):
    answer = 0
    # 상, 하 count
    for a in name:
        answer += min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)

    # 좌, 우 count
    idx = 0
    name = [a for a in name]
    while True:
        name[idx] = "A"
        if all([True if tmp == "A" else False for tmp in name]):
            break

        l, r = 1, 1
        while name[idx - l] == "A":
            l += 1
        while name[idx + r] == "A":
            r += 1

        answer += l if l < r else r
        idx -= l if l < r else r

    return answer


"""
# TEST CASE는 통과 못함
# 추가 TEST CASE는 통과

from collections import deque


def solution(name):
    answer = 0
    # 상, 하 count
    position = deque()
    for idx, a in enumerate(name):
        answer += min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)
        if not a == "A" and idx != 0:
            position.append(idx)

    if len(name) == 1:
        return answer

    # 좌, 우 count
    cur = 0
    while len(position) - 1:
        r, n_r = position[0], position[1]
        l, n_l = position[-1], position[-2]

        if abs(l - n_l) > abs(r - n_r):
            answer += len(name) - l + cur
            cur = position.pop()
        elif abs(l - n_l) == abs(r - n_r):
            if cur - l > 0:
                tmp_l = cur - l
            else:
                tmp_l = len(name) - l + cur

            if r - cur > 0:
                tmp_r = r - cur
            else:
                tmp_r = len(name) - cur + r

            if tmp_r < tmp_l:
                answer += tmp_r
                cur = position.pop()
            else:
                answer += tmp_l
                cur = position.popleft()

        else:
            if cur > r: answer += len(name) - cur + r
            else: answer += r - cur

            cur = position.popleft()

    return answer + min(abs(cur - position[0]), abs(len(name) - position[0] + cur))
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    names = ["BBABA",
             "BBBAAB",
             "BBAABAA",
             "BBAABBB",
             "BBAABAAAA",
             "BBAABAAAAB"]

    for name in names:
        print(solution(name))
