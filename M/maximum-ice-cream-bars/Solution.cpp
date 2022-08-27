// https://leetcode.com/problems/maximum-ice-cream-bars

class Solution {
 public:
  int maxIceCream(vector<int>& costs, int coins) {
    sort(costs.begin(), costs.end());

    int ret = 0;
    for (int c : costs)
      if (coins >= c) ++ret, coins -= c;
    return ret;
  }
};
