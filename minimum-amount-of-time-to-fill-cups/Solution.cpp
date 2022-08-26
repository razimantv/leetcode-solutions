// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

class Solution {
 public:
  int fillCups(vector<int>& amount) {
    int ret = 0;
    while (1) {
      sort(amount.begin(), amount.end());
      if (!amount.back()) break;
      ++ret;
      --amount[2];
      if (amount[1]) --amount[1];
    }
    return ret;
  }
};
