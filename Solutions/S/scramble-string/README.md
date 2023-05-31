# Scramble string

[Problem link](https://leetcode.com/problems/scramble-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/scramble-string

class Solution {
 public:
  string s1, s2;
  unordered_map<int, bool> cache;

  bool work(int i1, int j1, int i2, int j2) {
    int c = (i1 << 15) | (j1 << 10) | (i2 << 5) | j2;
    if (cache.count(c)) return cache[c];

    auto& ret = cache[c];
    auto S1 = s1.substr(i1, j1 - i1), S2 = s2.substr(i2, j2 - i2);
    {
      auto SS1 = S1;
      sort(SS1.begin(), SS1.end());
      auto SS2 = S2;
      sort(SS2.begin(), SS2.end());
      if (SS1 != SS2) return ret = false;
    }
    if (j1 - i1 == 1) return ret = true;
    for (int k1 = i1 + 1, k2 = i2 + 1, k2p = j2 - 1; k1 < j1;
         ++k1, ++k2, --k2p) {
      if ((work(i1, k1, i2, k2) and work(k1, j1, k2, j2)) or
          (work(i1, k1, k2p, j2) and work(k1, j1, i2, k2p)))
        return ret = true;
    }
    return ret = false;
  }
  bool isScramble(string s1, string s2) {
    this->s1 = s1;
    this->s2 = s2;

    return work(0, s1.size(), 0, s1.size());
  }
};
```