# Digit operations to make two integers equal

[Problem link](https://leetcode.com/problems/digit-operations-to-make-two-integers-equal)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/digit-operations-to-make-two-integers-equal

from sortedcontainers import SortedList


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def isprime(n):
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        if isprime(n):
            return -1

        cost = {n: n}
        sl = SortedList([(n, n)])

        def check(x, c):
            if isprime(x) or (x in cost and cost[x] <= c):
                return
            if x in cost:
                sl.remove((cost[x], x))
            cost[x] = c
            sl.add((c, x))

        while sl:
            c, x = sl.pop(0)
            if x == m:
                return c

            p, q = 1, 10
            while p <= x:
                suf = x % q
                if suf < q - p:
                    check(x + p, c + x + p)
                if suf >= p and x >= 2 * p:
                    check(x - p, c + x - p)
                p, q = q, 10 * q

        return -1
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove](/Collections/priority-queue.md#key-update-using-insert-and-remove)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Dijkstra's algorithm](/Collections/priority-queue.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)
