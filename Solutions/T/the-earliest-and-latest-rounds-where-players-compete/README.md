# The earliest and latest rounds where players compete

[Problem link](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete

class Solution {
 public:
  int n, p1, p2;
  set<int> cache, poss;
  void work(int mask, int round) {
    if (cache.count(mask)) return;
    cache.insert(mask);

    vector<int> cur;
    for (int i = 0; i < n; ++i)
      if (mask & (1 << i)) cur.push_back(i);

    for (int i = 0, j = cur.size() - 1; i <= j; ++i, --j)
      if ((cur[i] == p1 and cur[j] == p2) or (cur[i] == p2 and cur[j] == p1)) {
        poss.insert(round);
        return;
      }

    int M = (cur.size() + 1) >> 1;
    for (int i = 0; i < (1 << M); ++i) {
      int m = mask;
      for (int j = 0, l = 0, r = cur.size() - 1; j < M and l < r;
           ++j, ++l, --r) {
        int L = cur[l], R = cur[r];
        if (L == p1 or L == p2)
          m ^= (1 << R);
        else if (R == p1 or R == p2)
          m ^= (1 << L);
        else if ((i & (1 << j)))
          m ^= (1 << R);
        else
          m ^= (1 << L);
      }
      work(m, round + 1);
    }
  }
  vector<int> earliestAndLatest(int N, int P1, int P2) {
    n = N, p1 = --P1, p2 = --P2;
    work((1 << n) - 1, 1);
    return {*poss.begin(), *poss.rbegin()};
  }
};
```