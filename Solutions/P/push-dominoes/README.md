# Push dominoes

[Problem link](https://leetcode.com/problems/push-dominoes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/push-dominoes

class Solution {
 public:
  string pushDominoes(string dominoes) {
    vector<pair<char, int>> v;
    int n = dominoes.size();

    for (int i = 0; i < n; ++i)
      if (dominoes[i] != '.') v.push_back({dominoes[i], i});

    if (v.empty()) return dominoes;

    if (v[0].first == 'L')
      for (int i = 0; i < v[0].second; ++i) dominoes[i] = 'L';

    if (v.back().first == 'R')
      for (int i = v.back().second + 1; i < n; ++i) dominoes[i] = 'R';

    int m = v.size();
    for (int i = 1; i < m; ++i) {
      auto [cl, l] = v[i - 1];
      auto [cr, r] = v[i];

      if (cl == cr)
        for (int j = l + 1; j < r; ++j) dominoes[j] = cl;
      else if (cl == 'R')
        for (int j = l + 1, k = r - 1; j < k; ++j, --k)
          dominoes[j] = cl, dominoes[k] = cr;
    }
    return dominoes;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
