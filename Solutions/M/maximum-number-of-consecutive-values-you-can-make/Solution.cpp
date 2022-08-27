// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make

class Solution {
 public:
  int getMaximumConsecutive(vector<int>& coins) {
    sort(coins.begin(), coins.end());
    int tot = 0;
    for (int c : coins) {
      if (c > tot + 1) return tot + 1;
      tot += c;
    }
    return tot + 1;
  }
};
