// https://leetcode.com/problems/number-of-zero-filled-subarrays

class Solution {
 public:
  long long zeroFilledSubarray(vector<int>& nums) {
    long long ret{};
    for (int i = 0, start = -1, n = nums.size(); i < n; ++i)
      if (nums[i])
        start = i;
      else
        ret += i - start;
    return ret;
  }
};
