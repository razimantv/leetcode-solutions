// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

class Solution {
 public:
  int findMin(vector<int>& nums) {
    return *min_element(nums.begin(), nums.end());
  }
};
