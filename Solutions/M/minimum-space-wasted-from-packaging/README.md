# Minimum space wasted from packaging

[Problem link](https://leetcode.com/problems/minimum-space-wasted-from-packaging)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-space-wasted-from-packaging

class Solution {
 public:
  int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
    vector<pair<int, int>> all;
    for (int p : packages) all.push_back({p, -1});

    int B = boxes.size();
    for (int i = 0; i < B; ++i)
      for (int b : boxes[i]) all.push_back({b, i});

    sort(all.begin(), all.end());
    if (all.back().second == -1) return -1;

    vector<long long> last(B), best(B), psum(1);

    for (auto [w, id] : all) {
      if (id == -1) {
        psum.push_back(psum.back() + w);
        continue;
      }

      best[id] +=
          w * (psum.size() - 1 - last[id]) - (psum.back() - psum[last[id]]);
      last[id] = psum.size() - 1;
    }

    long long ans = LONG_LONG_MAX;
    for (int i = 0; i < B; ++i)
      if (last[i] == psum.size() - 1) ans = min(ans, best[i]);
    return ans % 1'000'000'007;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Sorting](/Collections/sorting.md#sorting) > [Queries and updates together](/Collections/sorting.md#queries-and-updates-together)
