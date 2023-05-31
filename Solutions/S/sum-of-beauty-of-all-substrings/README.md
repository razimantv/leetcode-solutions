# Sum of beauty of all substrings

[Problem link](https://leetcode.com/problems/sum-of-beauty-of-all-substrings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings

class Solution {
 public:
  int beautySum(string s) {
    int N = s.size(), beauty = 0;
    for (int i = 0; i < N; ++i) {
      vector<int> cnt(26, 0);
      for (int j = i; j < N; ++j) {
        cnt[s[j] - 'a']++;

        int M = 0, m = 10000;
        for (int n : cnt)
          if (n != 0) M = max(M, n), m = min(m, n);
        beauty += M - m;
      }
    }
    return beauty;
  }
};
```