# Find the minimum possible sum of a beautiful array

[Problem link](https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution {
 public:
  long long minimumPossibleSum(int n, int target) {
    long long ret{};
    unordered_set<int> seen;
    for (int i = 1; n; ++i) {
      if (!seen.count(target - i)) {
        ret += i;
        --n;
        seen.insert(i);
      }
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
