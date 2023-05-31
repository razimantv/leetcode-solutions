# Subarray sum equals k

[Problem link](https://leetcode.com/problems/subarray-sum-equals-k)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subarray-sum-equals-k

class Solution {
 public:
  int subarraySum(vector<int>& nums, int k) {
    map<long long, int> psum;
    psum[0] = 1;
    long long s = 0;
    int ret = 0;
    for (int n : nums) {
      s += n;
      ret += psum[s - k];
      psum[s]++;
    }
    return ret;
  }
};
```