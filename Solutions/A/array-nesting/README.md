# Array nesting

[Problem link](https://leetcode.com/problems/array-nesting)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/array-nesting

class Solution {
 public:
  int arrayNesting(vector<int>& nums) {
    int best = 0;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (nums[i] == -1) continue;
      int cur = 0, j = i;
      while (1) {
        ++cur;
        int temp = nums[j];
        nums[j] = -1;
        j = temp;
        if (j == i) break;
      }
      best = max(best, cur);
    }
    return best;
  }
};
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [Cycle](/Collections/permutation.md#cycle)
