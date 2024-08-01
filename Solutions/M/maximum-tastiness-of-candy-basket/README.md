# Maximum tastiness of candy basket

[Problem link](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution {
 public:
  int maximumTastiness(vector<int>& price, int k) {
    int n = price.size();
    sort(price.begin(), price.end());
    auto work = [&](int diff) {
      for (int i = 0, j = 1, x = 1; j < n; ++j) {
        if (price[j] - price[i] >= diff) {
          if (++x == k) return true;
          i = j;
        }
      }
      return false;
    };

    int start = 0, end = price.back() - price[0] + 1;
    while (end - start > 1) {
      int mid = (start + end) / 2;
      (work(mid) ? start : end) = mid;
    }
    return start;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Greedy](/Collections/greedy.md#greedy)
