// https://leetcode.com/problems/first-missing-positive

class Solution {
 public:
  int firstMissingPositive(vector<int>& nums) {
    int N = nums.size();
    for (int i = 0; i < N; ++i) {
      if (nums[i] > 0 and nums[i] <= N and nums[nums[i] - 1] != nums[i]) {
        swap(nums[i], nums[nums[i] - 1]);
        --i;
      }
    }

    for (int i = 0; i < N; ++i)
      if (nums[i] != i + 1) return i + 1;
    return N + 1;
  }
};
