# Sum multiples

[Problem link](https://leetcode.com/problems/sum-multiples/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-multiples/

class Solution {
 public:
  int sumOfMultiples(int n) {
    int ret{};
    for (int i = 1; i <= n; ++i)
      if (__gcd(i, 105) > 1) ret += i;
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
