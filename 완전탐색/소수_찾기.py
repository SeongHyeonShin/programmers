# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from itertools import permutations
from math import sqrt


def sieveofEratoshenes(N=0):
    prime_n = [i for i in range(N+1)]

    for i in range(2, int(sqrt(len(prime_n)))):
        if prime_n[i]:
            for j in range(i * 2, len(prime_n), i):
                prime_n[j] = 0

    prime_n[1] = 0
    return prime_n


def solution(numbers):
    perm = set([int(''.join(p)) for i in range(1, len(numbers) + 1) for p in permutations(numbers, i)])
    prime_number = sieveofEratoshenes(max(perm))
    return sum([1 for p in perm if prime_number[p]])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "011"
    print(solution(s))
