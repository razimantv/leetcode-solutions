# Minimum sum of mountain triplets i

[Problem link](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution {
 public:
  int minimumSum(vector<int>& nums) {
    int n = nums.size();
    vector<int> left(n, -1), right(n, -1);
    for (int i = 1, small = nums[0]; i < n; ++i) {
      if (small < nums[i])
        left[i] = small;
      else
        small = nums[i];
    }

    for (int i = n - 2, small = nums[n - 1]; i >= 0; --i) {
      if (small < nums[i])
        right[i] = small;
      else
        small = nums[i];
    }

    int best = -1;
    for (int i = 0; i < n; ++i) {
      if (left[i] == -1 or right[i] == -1) continue;
      int cur = left[i] + nums[i] + right[i];
      if (best == -1 or best > cur) best = cur;
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
