// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal

class Solution {
 public:
  int reductionOperations(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    if (nums[0] == nums.back()) return 0;

    int ret = 0, N = nums.size();
    for (int i = N - 2; i >= 0; --i)
      if (nums[i] != nums[i + 1]) ret += N - 1 - i;
    return ret;
  }
};
