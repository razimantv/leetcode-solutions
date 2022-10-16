// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution {
 public:
  long long countSubarrays(vector<int>& nums, int minK, int maxK) {
    int n = nums.size();
    long long ret{};
    for (int i = 0, mg = -1, mb = -1, Mg = -1, Mb = -1; i < n; ++i) {
      int x = nums[i];
      if (x == minK)
        mg = i;
      else if (x < minK)
        mb = i;
      if (x == maxK)
        Mg = i;
      else if (x > maxK)
        Mb = i;
      if (min(mg, Mg) < max(mb, Mb)) continue;
      ret += min(mg, Mg) - max(mb, Mb);
    }
    return ret;
  }
};
