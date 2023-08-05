// https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution {
 public:
  int accountBalanceAfterPurchase(int purchaseAmount) {
    int ret = 100 - purchaseAmount;
    if (ret % 10 > 5)
      ret += 10 - ret % 10;
    else
      ret -= ret % 10;
    return ret;
  }
};
