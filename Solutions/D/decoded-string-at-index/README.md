# Decoded string at index

[Problem link](https://leetcode.com/problems/decoded-string-at-index)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/decoded-string-at-index

class Solution {
 public:
  string decodeAtIndex(string S, int K) {
    while (1) {
      long long cur = 0;
      for (char c : S) {
        if (c < 'a') {
          if (cur * (c - '0') >= K) {
            K %= cur;
            if (K == 0) K = cur;
            break;
          } else
            cur *= c - '0';
        } else if (++cur == K)
          return string(1, c);
      }
    }
    return "";
  }
};
```