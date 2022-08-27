// https://leetcode.com/problems/remove-element

class Solution {
 public:
  int removeElement(vector<int>& nums, int val) {
    int N = nums.size();
    for (int i = 0; i < N;) {
      if (nums[i] == val) {
        for (int k = i; k + 1 < N; ++k) nums[k] = nums[k + 1];
        --N;
      } else
        ++i;
    }
    return N;
  }
};
