// https://leetcode.com/problems/max-consecutive-ones

class Solution {
 public:
  int findMaxConsecutiveOnes(vector<int>& nums) {
    int best = 0, cur = 0;
    for (int n : nums)
      if (n)
        best = max(best, ++cur);
      else
        cur = 0;
    return best;
  }
};
