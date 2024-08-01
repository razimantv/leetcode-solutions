# Check if point is reachable

[Problem link](https://leetcode.com/problems/check-if-point-is-reachable/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-point-is-reachable/

class Solution {
 public:
  bool isReachable(int x, int y) {
    if (x > y) swap(x, y);
    if (!x) return !(y & (y - 1));

    int g = __gcd(x, y);
    if (g & (g - 1)) return false;
    return true;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
