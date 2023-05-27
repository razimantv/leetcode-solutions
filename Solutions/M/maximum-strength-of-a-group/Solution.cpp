// https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution {
 public:
  long long maxStrength(vector<int>& nums) {
    long long ret = nums[0];
    for (int i = 1, n = nums.size(); i < (1 << n); ++i) {
      long long cur = 1;
      for (int j = 0; j < n; ++j)
        if (i & (1 << j)) cur *= nums[j];
      ret = max(ret, cur);
    }
    return ret;
  }
};
