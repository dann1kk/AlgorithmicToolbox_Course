def binary_search(keys, query, l, r):
    if l > r:
        return -1
    mid = (l + r) // 2
    if query == keys[mid]:
        return mid
    if query < keys[mid]:
        return binary_search(keys, query, l, mid - 1)
    else:
        return binary_search(keys, query, mid + 1, r)


if __name__ == '__main__':
    n = int(input())
    input_keys = list(map(int, input().split()))
    nq = int(input())
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search(input_keys, q, 0, len(input_keys) - 1), end=' ')
