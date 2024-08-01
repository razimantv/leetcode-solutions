# Bag of tokens

[Problem link](https://leetcode.com/problems/bag-of-tokens)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/bag-of-tokens

class Solution {
 public:
  int bagOfTokensScore(vector<int>& t, int P) {
    sort(t.begin(), t.end());
    int l = 0, r = t.size() - 1, s = 0;
    while (l <= r) {
      if (P >= t[l])
        P -= t[l++], ++s;
      else if (s and r > l)
        P += t[r--], --s;
      else
        break;
    }
    return s;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
