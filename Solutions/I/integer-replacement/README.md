# Integer replacement

[Problem link](https://leetcode.com/problems/integer-replacement)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/integer-replacement

class Solution {
 public:
  int integerReplacement(int n) {
    if (n < 3)
      return n - 1;
    else if (n & 1)
      return min(integerReplacement(n >> 1), integerReplacement((n >> 1) + 1)) +
             2;
    else
      return integerReplacement(n >> 1) + 1;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
