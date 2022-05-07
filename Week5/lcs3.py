import random


def lcs3_memo(dp, lst1, lst2, lst3, i, j, k):
    if i == len(lst1) or j == len(lst2) or k == len(lst3):
        return 0

    if dp[i][j][k] is not None:
        return dp[i][j][k]

    if lst1[i] == lst2[j] and lst2[j] == lst3[k]:
        dp[i][j][k] = 1 + lcs3_memo(dp, lst1, lst2, lst3, i+1, j+1, k+1)
        return dp[i][j][k]

    else:
        x = lcs3_memo(dp, lst1, lst2, lst3, i, j, k+1)
        y = lcs3_memo(dp, lst1, lst2, lst3, i, j+1, k)
        z = lcs3_memo(dp, lst1, lst2, lst3, i+1, j, k)
        max_lcs = max(x, y, z)
        dp[i][j][k] = max_lcs
        return max_lcs


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    dp = [[[None for i in range(len(third_sequence) + 1)]
           for j in range(len(second_sequence) + 1)]
          for k in range(len(first_sequence) + 1)]

    return lcs3_memo(dp, first_sequence, second_sequence, third_sequence, 0, 0, 0)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))