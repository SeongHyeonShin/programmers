# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        idx = 0

        for s in skill_tree:
            if s in skill:
                if s != skill[idx]:
                    break
                idx += 1
        else:
            answer += 1

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))
