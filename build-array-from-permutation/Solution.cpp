// https://leetcode.com/problems/build-array-from-permutation

class Solution {
 public:
  vector<int> buildArray(vector<int>& nums) {
    vector<int> ret(nums.size());
    for (int i = 0, n = nums.size(); i < n; ++i) ret[i] = nums[nums[i]];
    return ret;
  }
};
