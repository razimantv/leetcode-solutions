# Palindrome partitioning iv

[Problem link](https://leetcode.com/problems/palindrome-partitioning-iv)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/palindrome-partitioning-iv

class Solution {
 public:
  bool checkPartitioning(string s) {
    int L = s.size();
    vector<vector<char>> ispali(L, vector<char>(L, 0));
    for (int l = 1; l <= L; ++l) {
      for (int i = 0; i + l <= L; ++i) {
        if (l == 1)
          ispali[i][i] = 1;
        else if (l == 2)
          ispali[i][i + 1] = (s[i] == s[i + 1]);
        else
          ispali[i][i + l - 1] =
              (ispali[i + 1][i + l - 2] and (s[i] == s[i + l - 1]));
      }
    }

    vector<vector<char>> poss(L + 1, vector<char>(4, 0));
    poss[L][0] = 1;
    for (int i = L - 1; i >= 0; --i) {
      for (int j = i; j < L; ++j) {
        if (!ispali[i][j]) continue;
        for (int c = 1; c <= 3; ++c)
          if (poss[j + 1][c - 1]) poss[i][c] = true;
      }
    }
    return poss[0][3];
  }
};
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
