# Meeting rooms iii

[Problem link](https://leetcode.com/problems/meeting-rooms-iii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/meeting-rooms-iii/

class Solution {
 public:
  int mostBooked(int n, vector<vector<int>>& meetings) {
    vector<int> cnt(n);
    set<int> free;
    for (int i = 0; i < n; ++i) free.insert(i);
    set<pair<long long, int>> nextfree;
    sort(meetings.begin(), meetings.end());
    long long t{};
    int best = 0, bestroom = -1, m = meetings.size();
    for (int i = 0; i < m; ++i) {
      const auto& meet = meetings[i];
      t = max(t, (long long)meet[0]);
      while (!nextfree.empty() and nextfree.begin()->first <= t) {
        free.insert(nextfree.begin()->second);
        nextfree.erase(nextfree.begin());
      }

      if (free.empty()) {
        t = nextfree.begin()->first;
        --i;
        continue;
      }

      int room = *free.begin();
      ++cnt[room];
      free.erase(free.begin());
      nextfree.insert({t + meet[1] - meet[0], room});
    }
    for (int i = 0; i < n; ++i)
      if (best < cnt[i]) bestroom = i, best = cnt[i];
    return bestroom;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
