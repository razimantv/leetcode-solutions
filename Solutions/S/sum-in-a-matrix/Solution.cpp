// https://leetcode.com/problems/sum-in-a-matrix/

class Solution {
 public:
  int matrixSum(vector<vector<int>>& nums) {
    for (auto& row : nums) sort(row.begin(), row.end());
    int ret{};
    int n = nums[0].size();
    for (int i = 0; i < n; ++i) {
      int best{};
      for (const auto& row : nums) best = max(best, row[i]);
      ret += best;
    }
    return ret;
  }
};
