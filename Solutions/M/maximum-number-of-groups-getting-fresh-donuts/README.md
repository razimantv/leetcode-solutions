# Maximum number of groups getting fresh donuts

[Problem link](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts

class Solution {
 public:
  map<map<int, int>, int> cache;
  int work(map<int, int>& m, int pref, int B) {
    if (m.size() == 0) return 0;
    if (cache.count(m)) return cache[m];
    auto m2 = m;

    int best = 0;
    for (auto [x, c] : m) {
      if (c == 1)
        m2.erase(x);
      else
        --m2[x];

      best = max(best, (pref == 0) + work(m2, (pref + x + 1) % B, B));
      ++m2[x];
    }
    return cache[m] = best;
  }
  int maxHappyGroups(int B, vector<int>& groups) {
    map<int, int> cnt;
    int ans = 0;
    for (int& g : groups) {
      g %= B;
      if (g == 0)
        ++ans;
      else
        ++cnt[--g];
    }

    if (B % 2 == 0) {
      ans += cnt[B / 2 - 1] / 2;
      cnt[B / 2 - 1] %= 2;
      if (cnt[B / 2 - 1] == 0) cnt.erase(B / 2 - 1);
    }

    for (int i = 0, j = B - 2; i < j; ++i, --j) {
      int c = min(cnt[i], cnt[j]);
      ans += c;
      if ((cnt[i] -= c) == 0) cnt.erase(i);
      if ((cnt[j] -= c) == 0) cnt.erase(j);
    }

    return ans + work(cnt, 0, B);
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
* [Heuristic optimisation](/Collections/heuristic-optimisation.md#heuristic-optimisation)
