# Fruit into baskets

[Problem link](https://leetcode.com/problems/fruit-into-baskets)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/fruit-into-baskets

class Solution {
 public:
  int totalFruit(vector<int>& fruits) {
    vector<pair<int, int>> cnt;
    int ret = 0;
    for (int i = 0, j = 0, n = fruits.size(); j < n; ++j) {
      bool flag = false;
      for (auto& [k, v] : cnt) {
        if (k == fruits[j]) {
          ++v;
          flag = true;
          break;
        }
      }

      if (!flag) cnt.push_back({fruits[j], 1});

      while (cnt.size() > 2) {
        int cur = fruits[i++];
        for (auto& [k, v] : cnt) {
          if (k == cur) {
            if (--v == 0) {
              k = cnt.back().first;
              v = cnt.back().second;
              cnt.pop_back();
            }
            break;
          }
        }
      }

      ret = max(ret, j - i + 1);
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
