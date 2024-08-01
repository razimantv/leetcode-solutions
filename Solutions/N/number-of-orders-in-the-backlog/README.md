# Number of orders in the backlog

[Problem link](https://leetcode.com/problems/number-of-orders-in-the-backlog)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-orders-in-the-backlog

class Solution {
 public:
  map<int, long long> sell;
  map<int, long long, greater<int>> buy;
  long long processed;
  int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
    processed = 0;
    for (const auto& v : orders) {
      int price = v[0], amount = v[1], type = v[2];
      if (type == 0) {
        while (amount > 0 and !sell.empty()) {
          auto& [val, cnt] = *sell.begin();
          if (val > price) break;
          int sum = min(cnt, (long long)amount);
          amount -= sum;
          sell.begin()->second -= sum;
          processed += sum;
          if (cnt == 0) sell.erase(sell.begin());
        }
        if (amount) buy[price] += amount;
      } else {
        while (amount > 0 and !buy.empty()) {
          auto [val, cnt] = *buy.begin();
          if (val < price) break;
          int sum = min(cnt, (long long)amount);
          amount -= sum;
          buy.begin()->second -= sum;
          processed += sum;
          if (cnt == 0) buy.erase(buy.begin());
        }
        if (amount) sell[price] += amount;
      }
    }

    int ret = 0, MOD = 1'000'000'007;
    for (auto [val, cnt] : buy) ret = (ret + cnt) % MOD;
    for (auto [val, cnt] : sell) ret = (ret + cnt) % MOD;
    return ret;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
