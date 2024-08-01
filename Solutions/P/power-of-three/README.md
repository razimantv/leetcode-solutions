# Power of three

[Problem link](https://leetcode.com/problems/power-of-three)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/power-of-three

class Solution {
 public:
  bool isPowerOfThree(int n) {
    if (n <= 0) return false;
    while (n > 1) {
      if (n % 3) return false;
      n /= 3;
    }
    return true;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
