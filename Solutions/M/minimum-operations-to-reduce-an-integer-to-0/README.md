# Minimum operations to reduce an integer to 0

[Problem link](https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

class Solution {
 public:
  int minOperations(int n) {
    if (n == 1)
      return 1;
    else if ((n & 3) == 3)
      return 1 + minOperations(n + 1);
    else if (n & 1)
      return 1 + minOperations(n - 1);
    else
      return minOperations(n >> 1);
  }
};
```
## Tags

* [Bitwise operation](/README.md#Bitwise_operation)
* [Number transformations based on mathematical rules](/README.md#Number_transformations_based_on_mathematical_rules)
