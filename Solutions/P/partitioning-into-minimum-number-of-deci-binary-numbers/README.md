# Partitioning into minimum number of deci binary numbers

[Problem link](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution {
 public:
  int minPartitions(string n) {
    return (*max_element(n.begin(), n.end())) - '0';
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
