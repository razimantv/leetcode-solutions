# Maximum product subarray

[Problem link](https://leetcode.com/problems/maximum-product-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-product-subarray

class Solution {
 public:
  int maxProduct(vector<int>& nums) {
    int best = nums[0], m = 0, cur = 1;
    for (int n : nums) {
      best = max(best, n);
      if (n == 0)
        m = 0, cur = 1;
      else {
        cur *= n;
        if (cur > 0)
          best = max(best, cur);
        else if (m)
          best = max(best, cur / m);
        else
          m = cur;
      }
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
