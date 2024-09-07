# Online stock span

[Problem link](https://leetcode.com/problems/online-stock-span)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/online-stock-span

class StockSpanner {
 public:
  int cnt;
  vector<pair<int, int>> dec;
  StockSpanner() {
    cnt = 0;
    dec = vector<pair<int, int>>(1, {1e6, 0});
  }

  int next(int price) {
    while (dec.back().first <= price) dec.pop_back();
    int ret = ++cnt - dec.back().second;
    dec.push_back({price, cnt});
    return ret;
  }
};

```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
