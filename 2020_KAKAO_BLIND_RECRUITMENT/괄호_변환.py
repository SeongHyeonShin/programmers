# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def iscorrect(s):
    c = 0

    for par in s:
        c += 1 if par == '(' else -1
        if c < 0: return False

    return True


def solution(p):
    answer = ''

    while True:
        if iscorrect(p):
            return answer + p

        idx, count = 0, 0
        for par in p:
            idx += 1 if par == '(' else -1

            count += 1
            if idx == 0:
                break

        u, v = p[:count], p[count:]

        if iscorrect(u):
            answer += u
            p = v
        else:
            v = solution(v)
            u = u[1:-1]
            tmp_u = ''
            for tmp in u:
                tmp_u += '(' if tmp == ')' else ')'
            p = '(' + v + ')' + tmp_u

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = "()))((()"
    print(solution(p))
