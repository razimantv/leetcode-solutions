// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
 public:
  int removeDuplicates(vector<int>& nums) {
    int N = nums.size();
    for (int i = 1; i < N;) {
      if (nums[i] == nums[i - 1]) {
        for (int k = i; k + 1 < N; ++k) nums[k] = nums[k + 1];
        --N;
      } else
        ++i;
    }
    return N;
  }
};
