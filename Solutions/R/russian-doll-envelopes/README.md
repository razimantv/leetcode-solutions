# Russian doll envelopes

[Problem link](https://leetcode.com/problems/russian-doll-envelopes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/russian-doll-envelopes

class Solution {
 public:
  int maxEnvelopes(vector<vector<int>>& envelopes) {
    sort(envelopes.begin(), envelopes.end(),
         [](const vector<int>& u, const vector<int>& v) {
           if (u[0] != v[0]) return u[0] < v[0];
           return u[1] > v[1];
         });
    vector<int> lis;
    for (auto u : envelopes) {
      auto vit = lower_bound(lis.begin(), lis.end(), u[1]);
      if (vit != lis.end())
        *vit = u[1];
      else
        lis.push_back(u[1]);
    }

    return lis.size();
  }
};
```