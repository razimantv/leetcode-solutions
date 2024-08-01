# Number of employees who met the target

[Problem link](https://leetcode.com/problems/number-of-employees-who-met-the-target/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
 public:
  int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
    int ret{};
    for (int x : hours) ret += (x >= target);
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
