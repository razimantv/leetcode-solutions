# Reach a number

[Problem link](https://leetcode.com/problems/reach-a-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reach-a-number

class Solution {
 public:
  int reachNumber(int target) {
    if (target < 0) target = -target;
    int ret = 0, tot = 0;
    while (tot < target or ((tot - target) & 1)) tot += ++ret;
    return ret;
  }
};
```
## Tags

* [Number transformations based on mathematical rules](/Collections/number-transformations-based-on-mathematical-rules.md#number-transformations-based-on-mathematical-rules)
