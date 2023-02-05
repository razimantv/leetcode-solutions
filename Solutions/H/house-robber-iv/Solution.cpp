// https://leetcode.com/problems/house-robber-iv/

class Solution {
 public:
  int minCapability(vector<int>& nums, int k) {
    int start = 0, end = *max_element(nums.begin(), nums.end());
    while (end - start > 1) {
      int mid = (start + end) / 2, prev = 0, cur = 0;
      for (int x : nums) {
        swap(prev, cur);
        cur = max(prev, cur + (x <= mid));
      }
      (cur >= k ? end : start) = mid;
    }
    return end;
  }
};
