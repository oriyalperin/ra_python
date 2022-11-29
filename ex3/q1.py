def bounded_subsets(S, C):
    def bss_rec(first, i):
        yield first
        for k in range(i, len(S)):
            subset_sum = sum(first) + S[k]
            if subset_sum <= C:
                f = first.copy()
                f.append(S[k])
                yield from bss_rec(f, k + 1)
            else:
                break

    S = sorted(S)
    yield from bss_rec([], 0)


def bounded_subsets2(S, C):
    def bss_rec(first, i, j):
        if S[j] - 1 < sum(first):
            yield first
        for k in range(i, len(S)):
            subset_sum = sum(first) + S[k]
            if subset_sum <= S[j]:
                f = first.copy()
                f.append(S[k])
                yield from bss_rec(f, k + 1, j)

    S = sorted(S)
    yield []

    for j in range(0, len(S)):
        if S[j] > C:
            break
        yield from bss_rec([], 0, j)


"""bss_rec([], [4, 3, 1, 2], 4, 0)
for i in bss_rec([], [1, 2, 3, 4, 5, 6, 7], 9, 0):
    print(i)
for s in bss_rec([],range(50,150), 103,0):
    print(s)
"""
"""for i in bounded_subsets2([1, 2, 3, 4, 5, 6, 7], 9):
    print(i)"""

for s in bounded_subsets2(range(50, 150), 103):
    print(s)
for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
    print(s)
for s in bounded_subsets2(range(100), 1000000000000):
    print(s)