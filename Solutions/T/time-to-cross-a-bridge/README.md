# Time to cross a bridge

[Problem link](https://leetcode.com/problems/time-to-cross-a-bridge/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/time-to-cross-a-bridge/

class Solution {
 public:
  int findCrossingTime(int n, int k, vector<vector<int>>& time) {
    vector<int> efficiency(k);
    auto cmp = [&](int i, int j) {
      if (efficiency[i] != efficiency[j]) return efficiency[i] > efficiency[j];
      return i > j;
    };
    set<int, decltype(cmp)> left(cmp), right(cmp);
    for (int i = 0; i < k; ++i) {
      efficiency[i] = time[i][0] + time[i][2];
      left.insert(i);
    }

    int processing = 0, t = 0, tt = 0;
    set<tuple<int, int, int>> toadd;
    while (n or processing) {
      while (!toadd.empty()) {
        auto [tt, worker, pq] = *toadd.begin();
        if (tt > t) break;
        toadd.erase(toadd.begin());
        (pq ? right : left).insert(worker);
        if (!pq and --processing == 0 and !n) goto BPP;
      }
      if (!right.empty()) {
        int worker = *right.begin();
        right.erase(right.begin());
        tt = t += time[worker][2];
        toadd.insert({t + time[worker][3], worker, 0});
      } else if (!left.empty() and n) {
        int worker = *left.begin();
        left.erase(left.begin());
        --n;
        ++processing;
        t += time[worker][0];
        toadd.insert({t + time[worker][1], worker, 1});
      } else {
        auto [tt, worker, pq] = *toadd.begin();
        t = tt;
      }
    }

  BPP:
    return tt;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
