# Design a stack with increment operation

[Problem link](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, n: int):
        self.n = n
        self.ar = []

    def push(self, x: int) -> None:
        if len(self.ar) < self.n:
            self.ar.append(x)

    def pop(self) -> int:
        return self.ar.pop() if self.ar else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.ar))):
            self.ar[i] += val
```
## Tags

* [Stack](/Collections/stack.md#stack)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
