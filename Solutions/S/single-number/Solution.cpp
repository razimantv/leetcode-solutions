// https://leetcode.com/problems/single-number

class Solution {
 public:
  int singleNumber(vector<int>& nums) {
    return std::accumulate(nums.begin(), nums.end(), 0,
                           [](int a, int b) { return a ^ b; });
  }
};
