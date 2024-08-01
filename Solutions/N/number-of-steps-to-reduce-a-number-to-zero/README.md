# Number of steps to reduce a number to zero

[Problem link](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution {
 public:
  int numberOfSteps(int num) {
    if (num == 0)
      return 0;
    else if (num & 1)
      return 1 + numberOfSteps(num - 1);
    else
      return 1 + numberOfSteps(num / 2);
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
