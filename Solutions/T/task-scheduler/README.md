# Task scheduler

[Problem link](https://leetcode.com/problems/task-scheduler)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/task-scheduler

class Solution {
 public:
  int leastInterval(vector<char>& tasks, int n) {
    ++n;
    int cnt[26] = {0};
    for (auto c : tasks) cnt[c - 'A']++;
    map<int, int> cnt2;
    for (int i = 0; i < 26; ++i) cnt2[cnt[i]]++;

    int L = cnt2.rbegin()->first, M = min(cnt2.rbegin()->second, n);
    return max((int)tasks.size(), n * (L - 1) + M);
  }
};
```