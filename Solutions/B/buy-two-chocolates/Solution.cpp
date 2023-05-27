// https://leetcode.com/problems/buy-two-chocolates/

class Solution {
 public:
  int buyChoco(vector<int>& prices, int money) {
    nth_element(prices.begin(), prices.begin() + 1, prices.end());
    int two = prices[0] + prices[1];
    if (two > money) return money;
    return money - two;
  }
};
