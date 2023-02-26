// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

class Solution {
 public:
  int maxNumOfMarkedIndices(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    auto poss = [&](int k) {
      for (int i = 0, j = n - k; j < n; ++i, ++j)
        if ((nums[i] << 1) > nums[j]) return false;
      return true;
    };
    int start = 0, end = n / 2 + 1;
    while (end - start > 1) {
      int mid = (start + end) >> 1;
      (poss(mid) ? start : end) = mid;
    }
    return start << 1;
  }
};
