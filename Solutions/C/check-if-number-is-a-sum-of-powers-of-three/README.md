# Check if number is a sum of powers of three

[Problem link](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

class Solution {
 public:
  bool checkPowersOfThree(int n) {
    int p = 1;
    while (p <= n) p *= 3;
    p /= 3;

    while (p) {
      if (n >= p) n -= p;
      p /= 3;
    }
    return n == 0;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
