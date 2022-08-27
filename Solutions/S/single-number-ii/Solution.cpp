// https://leetcode.com/problems/single-number-ii

class Solution {
 public:
  int singleNumber(vector<int>& nums) {
    unordered_map<int, int> cnt;
    for (auto n : nums) cnt[n]++;
    for (auto m : cnt)
      if (m.second == 1) return m.first;
    return 0;
  }
};
