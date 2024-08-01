# Smallest sufficient team

[Problem link](https://leetcode.com/problems/smallest-sufficient-team/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-sufficient-team/

class Solution {
 public:
  vector<int> smallestSufficientTeam(vector<string>& skills,
                                     vector<vector<string>>& people) {
    int s = skills.size(), skillmask = (1 << s) - 1, n = people.size();
    long long peoplemask = (1ll << n) - 1;
    auto better = [](long long m1, long long m2) {
      return __builtin_popcountll(m1) < __builtin_popcountll(m2) ? m1 : m2;
    };

    unordered_map<string, int> m;
    for (int i = 0; i < s; ++i) m[skills[i]] = i;

    vector<long long> best(skillmask + 1, peoplemask);
    best[0] = 0;
    for (int i = 0; i < n; ++i) {
      int pskill{};
      for (auto& skill : people[i]) pskill |= (1 << m[skill]);
      for (int m = 0; m <= skillmask; ++m)
        best[m] = better(best[m], best[m & (skillmask ^ pskill)] | (1ll << i));
    }
    vector<int> ret;
    for (int i = 0; i < n; ++i)
      if (best[skillmask] & (1ll << i)) ret.push_back(i);
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
