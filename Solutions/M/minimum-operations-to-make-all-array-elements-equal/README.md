# Minimum operations to make all array elements equal

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution {
 public:
  vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<long long> psum(n + 1);
    for (int i = 0; i < n; ++i) psum[i + 1] = psum[i] + nums[i];

    vector<long long> ret;
    for (int q : queries) {
      long long pos = lower_bound(nums.begin(), nums.end(), q) - nums.begin();
      ret.push_back(q * pos - psum[pos] + psum.back() - psum[pos] -
                    q * (n - pos));
    }
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
