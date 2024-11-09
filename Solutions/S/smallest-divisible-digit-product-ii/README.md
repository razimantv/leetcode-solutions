# Smallest divisible digit product ii

[Problem link](https://leetcode.com/problems/smallest-divisible-digit-product-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

class Solution:
    def smallestNumber(self, num: str | list[int], t: int) -> str:
        def split_count(x):
            cnt = []
            for p in [2, 3, 5, 7]:
                cur = 0
                while x % p == 0:
                    cur += 1
                    x //= p
                cnt.append(cur)
            return x, cnt

        t, cnt = split_count(t)
        if t > 1:
            return "-1"

        digcnt = [[]] + [split_count(d)[1] for d in range(1, 10)]

        def digoptions(cnt):
            return [
                [
                    [9, (cnt[1] + 1) // 2], [8, (cnt[0] + 2) // 3],
                    [7, cnt[3]], [5, cnt[2]]
                ],
                [
                    [9, cnt[1] // 2], [8, (cnt[0] + 1) // 3], [7, cnt[3]],
                    [6, 1], [5, cnt[2]]
                ]
            ]

        def minlength(cnt):
            dcnt = digoptions(cnt)
            return min(sum(v for d, v in dc) for dc in dcnt)

        def poss(i, cnt, tocompare=True):
            options = digoptions(cnt)
            dcnt = options[1 if sum(c for x, c in options[0]) > n - i else 0]
            dtot = sum(c for x, c in dcnt)
            if dtot > n - i:
                return False
            elif not tocompare:
                return True

            dcnt[0][1] += n - i - dtot
            for x, c in dcnt:
                for j in range(c):
                    if num[i] == x:
                        i += 1
                    else:
                        return num[i] < x
            return True

        L, n = minlength(cnt), len(num)
        if L <= n:
            num = [0] + [int(d) for d in num]
            n += 1
            cntsub = [cnt, cnt]
            for i in range(1, n):
                d = num[i]
                if not d:
                    break

                cur = [max(p - x, 0) for p, x in zip(cntsub[-1], digcnt[d])]
                if not sum(cur):
                    break

                cntsub.append(cur)

            start, end, no0 = 0, n, True
            for i in range(1, n):
                if num[i] == 0:
                    end, no0 = i + 1, False
                    break

            if no0 and len(cntsub) <= n:
                return ''.join(str(d) for d in num[1:])

            while end - start > 1:
                mid = (end + start) // 2
                if poss(mid, [0] * 4 if mid >= len(cntsub) else cntsub[mid]):
                    start = mid
                else:
                    end = mid

            cnt = [0] * 4 if start >= len(cntsub) else cntsub[start]
        else:
            num = [0] * (L - n) + [int(d) for d in num]
            n, start = L, 0

        for i in range(start, n):
            for d in range((num[i] if i == start else 0) + 1, 10):
                num[i] = d
                cp = [max(p - x, 0) for p, x in zip(cnt, digcnt[d])]
                if poss(i + 1, cp, False):
                    cnt = cp
                    break

        return ''.join(str(d) for d in (num if num[0] else num[1:]))
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Greedy](/Collections/greedy.md#greedy)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
