# Integer break

[Problem link](https://leetcode.com/problems/integer-break)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/integer-break

class Solution {
 public:
  int integerBreak(int n) {
    if (n < 4)
      return n - 1;
    else if (n == 4)
      return 4;
    int ret = 1;
    while (n > 4) n -= 3, ret *= 3;
    return ret * n;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
