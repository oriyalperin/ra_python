def bounded_subsets(S: list, C: int):
    """
    generator of all S subsets that their sum is up to C.
    :param S: list of positive numbers
    :param C: a positive number

    >>> for s in bounded_subsets(range(1, 5), 5):
    ...     print(s)
    []
    [1]
    [1, 2]
    [1, 3]
    [1, 4]
    [2]
    [2, 3]
    [3]
    [4]
    """

    def bss_rec(subset, i):
        """
        inner generator. find the next item recursively.
        develop each subset by using the previous relevant subset and the next item in S.
        if current subset sum > C, then we stop developing this subset.

        :param subset: previous subset
        :param i: next item index
        """
        yield subset
        for k in range(i, len(S)):
            subset_sum = sum(subset) + S[k]
            if subset_sum <= C:
                f = subset.copy()
                f.append(S[k])
                yield from bss_rec(f, k + 1)
            else:
                break

    S = sorted(S)
    yield from bss_rec([], 0)


def bounded_subsets2(S, C):
    """
    generator of all S subsets that their sum is up to C, ordered by the subset sum.
    pass all S items and develop all subsets that their sum < current S item.
    :param S: list of positive numbers
    :param C: a positive number

    tests:

    >>> for s in bounded_subsets2(range(1, 6), 5):
    ...     print(s)
    []
    [1]
    [2]
    [1, 2]
    [3]
    [1, 3]
    [4]
    [1, 4]
    [2, 3]
    [5]
    """

    def bss_rec(subset, i, j):
        """
        inner generator. find the next item recursively.
        develop each subset by using the previous relevant subset and the next item in S.
        if current subset sum > C, then we stop developing this subset.


        :param subset: previous subset
        :param i: next item index
        :param j: the sum subset bound
        """
        if valueof(j) - 1 < sum(subset):
            yield subset
        for k in range(i, len(S)):
            subset_sum = sum(subset) + S[k]
            if subset_sum <= valueof(j):
                f = subset.copy()
                f.append(S[k])
                yield from bss_rec(f, k + 1, j)
            else:
                break

    S = sorted(S)
    valueof = lambda j: S[j]
    yield []
    for j in range(0, len(S)):
        if S[j] > C:
            break
        yield from bss_rec([], 0, j)

    max_val = S[len(S) - 1]
    if C > max_val:
        valueof = lambda j: j
        for j in range(max_val, C + 1):
            yield from bss_rec([], 0, j)
