// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution {
 public:
  vector<int> findDuplicates(vector<int>& nums) {
    vector<int> ret;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] == i + 1 or nums[i] == 0) continue;
      if (nums[nums[i] - 1] == nums[i]) {
        ret.push_back(nums[i]);
        nums[i] = 0;
      } else {
        swap(nums[i], nums[nums[i] - 1]);
        --i;
      }
    }
    return ret;
  }
};
