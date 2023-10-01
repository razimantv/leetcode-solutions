// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution {
 public:
  int maxSubarrays(vector<int>& nums) {
    int zero = INT_MAX, n = nums.size();
    vector<int> last(20, -1), best(n, 1);
    for (int i = 0; i < n; ++i) {
      int small = i;
      for (int j = 0; j < 20; ++j) {
        if ((nums[i] & (1 << j)) == 0) last[j] = i;
        small = min(small, last[j]);
      }
      if (small != -1 and zero > n) zero = i;
      if (small > zero) best[i] = best[small - 1] + 1;
    }
    return best.back();
  }
};
