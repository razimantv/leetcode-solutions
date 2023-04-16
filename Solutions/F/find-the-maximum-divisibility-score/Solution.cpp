// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
 public:
  int maxDivScore(vector<int>& nums, vector<int>& divisors) {
    int best, val{-1};
    sort(divisors.begin(), divisors.end());
    for (int x : divisors) {
      int cnt{};
      for (int y : nums)
        if (y % x == 0) ++cnt;
      if (cnt > val) val = cnt, best = x;
    }
    return best;
  }
};
