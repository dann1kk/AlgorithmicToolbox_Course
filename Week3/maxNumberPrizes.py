def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    prizes = []

    curr_prize = 1
    while n > 0:
        if curr_prize <= n:
            prizes.append(curr_prize)
            n -= curr_prize
            curr_prize += 1
        else:
            if prizes[-1] < n:
                prizes.append(n)
            else:
                prizes[-1] += n
            break

    return prizes


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)