def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements, l, r):

    if l >= r:
        return elements[l]

    mid = (l + r) // 2
    l_cand = majority_element(elements, l, mid)
    r_cand = majority_element(elements, mid + 1, r)

    if l_cand == -1 and r_cand == -1:
        return -1

    l_count, r_count = 0, 0
    for i in range(l, r+1):
        if elements[i] == l_cand:
            l_count += 1
            if l_count > ((r + 1) - l) // 2:
                return l_cand
        if elements[i] == r_cand:
            r_count += 1
            if r_count > ((r + 1) - l) // 2:
                return r_cand

    return -1


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(int(majority_element(input_elements, 0, input_n - 1) != -1))