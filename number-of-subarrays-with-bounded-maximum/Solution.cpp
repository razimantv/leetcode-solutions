// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum

class Solution {
 public:
  int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
    int bad = -1, good = -1, ret = 0;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      int x = nums[i];
      if (x > right) bad = i;
      if (x >= left) good = i;
      ret += good - bad;
    }
    return ret;
  }
};
