// https://leetcode.com/problems/move-zeroes

class Solution {
 public:
  void moveZeroes(vector<int>& nums) {
    int next = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] != 0) nums[next++] = nums[i];
    }
    while (next < nums.size()) nums[next++] = 0;
  }
};
