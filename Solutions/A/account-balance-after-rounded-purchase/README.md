# Account balance after rounded purchase

[Problem link](https://leetcode.com/problems/account-balance-after-rounded-purchase/)

## Solutions


### Solution.cpp
```cpp
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
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
