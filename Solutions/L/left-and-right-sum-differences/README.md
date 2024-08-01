# Left and right sum differences

[Problem link](https://leetcode.com/problems/left-and-right-sum-differences/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
 public:
  vector<int> leftRigthDifference(vector<int>& nums) {
    int n = nums.size();
    vector<int> ret(n);
    for (int i = 1, pref = 0; i < n; ++i) ret[i] = (pref += nums[i - 1]);
    for (int i = n - 2, pref = 0; i >= 0; --i)
      ret[i] = abs(ret[i] - (pref += nums[i + 1]));
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
