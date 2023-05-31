# Maximum ascending subarray sum

[Problem link](https://leetcode.com/problems/maximum-ascending-subarray-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution {
 public:
  int maxAscendingSum(vector<int>& nums) {
    int N = nums.size();
    vector<int> best(N);

    int ret = 0;
    for (int i = 0; i < N; ++i) {
      best[i] = nums[i];
      if (i > 0 and nums[i - 1] < nums[i]) best[i] += best[i - 1];
      ret = max(ret, best[i]);
    }
    return ret;
  }
};
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
