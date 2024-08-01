# Find the score of all prefixes of an array

[Problem link](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
 public:
  vector<long long> findPrefixScore(vector<int>& nums) {
    int n = nums.size();
    vector<long long> ret(n);
    ret[0] = nums[0] * 2;
    for (int i = 1; i < n; ++i) {
      int cur = nums[i];
      nums[i] = max(nums[i - 1], cur);
      ret[i] = ret[i - 1] + cur + nums[i];
    }
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
