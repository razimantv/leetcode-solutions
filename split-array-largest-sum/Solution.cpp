// https://leetcode.com/problems/split-array-largest-sum

class Solution {
 public:
  bool poss(const vector<int>& nums, int tot, int m) {
    for (int i = 0, n = nums.size(), cur = 0; i < n; ++i) {
      if ((cur += nums[i]) > tot) {
        if (!--m) return false;
        cur = nums[i];
      }
    }
    return true;
  }
  int splitArray(const vector<int>& nums, int m) {
    int start = 0, end = 0;
    for (int x : nums) start = max(start, x), end += x;
    --start;

    while (end - start > 1) {
      int mid = (end + start) >> 1;
      (poss(nums, mid, m) ? end : start) = mid;
    }
    return end;
  }
};
