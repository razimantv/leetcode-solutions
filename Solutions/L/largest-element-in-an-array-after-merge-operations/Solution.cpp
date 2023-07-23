// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution {
 public:
  long long maxArrayValue(vector<int>& nums) {
    long long cur{}, best{};
    for (int n = nums.size(), i = n - 1; i >= 0; --i) {
      if (nums[i] <= cur)
        cur += nums[i];
      else
        cur = nums[i];
      best = max(best, cur);
    }
    return best;
  }
};
