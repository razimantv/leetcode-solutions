// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
 public:
  int removeDuplicates(vector<int>& nums) {
    int N = nums.size(), j = 1;
    for (int i = 1; i < N; ++i)
      if (nums[i] != nums[j - 1]) nums[j++] = nums[i];
    return j;
  }
};
