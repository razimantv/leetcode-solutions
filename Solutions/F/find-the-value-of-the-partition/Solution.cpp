// https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution {
 public:
  int findValueOfPartition(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int ret{INT_MAX};
    for (int i = 1, n = nums.size(); i < n; ++i)
      ret = min(ret, nums[i] - nums[i - 1]);
    return ret;
  }
};
