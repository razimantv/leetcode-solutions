# Search suggestions system

[Problem link](https://leetcode.com/problems/search-suggestions-system)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/search-suggestions-system

class Solution {
 public:
  vector<vector<string>> suggestedProducts(vector<string>& products,
                                           string searchWord) {
    sort(products.begin(), products.end());
    int L = searchWord.size();
    vector<vector<string>> ret(L);

    for (int l = 1, L = searchWord.size(); l <= L; ++l) {
      auto cur = searchWord.substr(0, l);
      auto vit = lower_bound(products.begin(), products.end(), cur);
      for (int i = 0; i < 3 and vit != products.end(); ++i, ++vit) {
        bool flag = true;
        for (int j = 0; j < l; ++j) {
          if (cur[j] != (*vit)[j]) {
            flag = false;
            break;
          }
        }
        if (flag)
          ret[l - 1].push_back(*vit);
        else
          break;
      }
      if (ret[l - 1].empty()) break;
    }
    return ret;
  }
};
```