# Remove duplicate letters

[Problem link](https://leetcode.com/problems/remove-duplicate-letters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-duplicate-letters

class Solution {
 public:
  string removeDuplicateLetters(string s) {
    int N = s.size();
    int C = 0;

    vector<int> mask(N + 1, 0), pos[26];
    for (int i = N - 1; i >= 0; --i) {
      char c = s[i] - 'a';
      if (pos[c].empty()) ++C;
      pos[c].push_back(i);
      mask[i] = mask[i + 1] | (1 << c);
    }

    string ret;
    int last = -1, remmask = 0;
    while (C--) {
      for (char i = 0; i < 26; ++i) {
        if (remmask & (1 << i)) continue;
        while (!pos[i].empty() and pos[i].back() <= last) pos[i].pop_back();
        if (pos[i].empty()) continue;
        int cur = mask[pos[i].back() + 1] & (~(remmask | (1 << i)));
        if (__builtin_popcount(cur) < C) continue;
        remmask |= (1 << i);
        last = pos[i].back();
        ret += 'a' + i;
      }
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Greedy](/Collections/greedy.md#greedy)
* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
