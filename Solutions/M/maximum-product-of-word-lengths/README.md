# Maximum product of word lengths

[Problem link](https://leetcode.com/problems/maximum-product-of-word-lengths)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-product-of-word-lengths

class Solution {
 public:
  int maxProduct(vector<string>& words) {
    int N = words.size(), best = 0;
    vector<int> mask(N);
    for (int i = 0; i < N; ++i)
      for (char c : words[i]) mask[i] |= (1 << (c - 'a'));
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < i; ++j)
        if ((mask[i] & mask[j]) == 0)
          best = max(best, (int)(words[i].size() * words[j].size()));
    return best;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
