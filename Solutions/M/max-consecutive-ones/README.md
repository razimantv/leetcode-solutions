# Max consecutive ones

[Problem link](https://leetcode.com/problems/max-consecutive-ones)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/max-consecutive-ones

class Solution {
 public:
  int findMaxConsecutiveOnes(vector<int>& nums) {
    int best = 0, cur = 0;
    for (int n : nums)
      if (n)
        best = max(best, ++cur);
      else
        cur = 0;
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
