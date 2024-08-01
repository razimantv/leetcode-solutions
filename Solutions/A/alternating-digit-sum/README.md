# Alternating digit sum

[Problem link](https://leetcode.com/problems/alternating-digit-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
 public:
  int alternateDigitSum(int n) {
    int ret{};
    while (n) ret = n % 10 - ret, n /= 10;
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
