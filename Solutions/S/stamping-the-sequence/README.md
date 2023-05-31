# Stamping the sequence

[Problem link](https://leetcode.com/problems/stamping-the-sequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stamping-the-sequence

class Solution {
 public:
  int N, M;
  vector<int> fwmatch, bwmatch;
  vector<pair<int, int>> maxmatch;
  map<pair<int, int>, vector<int>> cache;
  vector<int> movesToStamp(const string& stamp, const string& target,
                           int start = 0, int end = -1) {
    if (end == -1) {
      N = target.size();
      M = stamp.size();
      end = N - 1;
      fwmatch = vector<int>(N, 0), bwmatch = fwmatch;
      maxmatch = vector<pair<int, int>>(N, {0, -1});
      for (int i = 0; i + M <= N; ++i) {
        for (int j = 0; j < M; ++j) {
          if (target[i + j] == stamp[j])
            ++fwmatch[i];
          else
            break;
        }
      }

      for (int i = N - 1; i >= M - 1; --i) {
        for (int j = M - 1; j >= 0; --j) {
          if (target[i + j - M + 1] == stamp[j])
            ++bwmatch[i];
          else
            break;
        }
      }

      for (int i = 0; i <= N - M; ++i) {
        for (int j = 0, cur = 0; j < M; ++j) {
          if (target[i + j] == stamp[j]) {
            if (++cur > maxmatch[i + j].first) maxmatch[i + j] = {cur, i};
          } else
            cur = 0;
        }
      }
    }

    if (cache.count({start, end})) return cache[{start, end}];

    if (maxmatch[end].first >= end - start + 1)
      return cache[{start, end}] = {maxmatch[end].second};

    for (int i = start; i <= end and i < start + M - 1; ++i) {
      if (bwmatch[i] < i - start + 1) continue;
      if (i == end) return cache[{start, end}] = {end - M + 1};
      auto cur = movesToStamp(stamp, target, i + 1, end);
      if (cur.empty()) continue;
      cur.push_back(i - M + 1);
      return cache[{start, end}] = cur;
    }

    for (int i = end; i >= start and i > end - M + 1; --i) {
      if (fwmatch[i] < end - i + 1) continue;
      if (i == start) return cache[{start, end}] = {start};
      auto cur = movesToStamp(stamp, target, start, i - 1);
      if (cur.empty()) continue;
      cur.push_back(i);
      return cache[{start, end}] = cur;
    }

    for (int i = start; i <= end - M + 1; ++i) {
      if (fwmatch[i] < M) continue;
      vector<int> left, right;
      if (i > start and
          (left = movesToStamp(stamp, target, start, i - 1)).empty())
        continue;
      if (i < end - M + 1 and
          (right = movesToStamp(stamp, target, i + M, end)).empty())
        continue;
      for (int x : right) left.push_back(x);
      left.push_back(i);
      return cache[{start, end}] = left;
    }
    return cache[{start, end}] = {};
  }
};
```