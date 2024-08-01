# Interleaving string

[Problem link](https://leetcode.com/problems/interleaving-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/interleaving-string

class Solution {
 public:
  bool isInterleave(string s1, string s2, string s3) {
    int M = s1.size(), N = s2.size(), T = s3.length();
    if (M + N != T) return false;

    // dp(i,j) = s1(0…i) and s2(0…j) give s3(0…i+j)
    // dp(i,j) = (s1(i) = s3(i+j) and dp(i-1,j)) or (s2(j)=s3(i+j) and
    // dp(i,j-1))
    vector<char> poss(N + 1);
    poss[0] = 1;
    for (int i = 0; i < N; ++i)
      if (s2[i] == s3[i])
        poss[i + 1] = 1;
      else
        break;

    for (int i = 0; i < M; ++i) {
      poss[0] = (s1[i] == s3[i]) and poss[0];
      for (int j = 0; j < N; ++j) {
        poss[j + 1] = (((s3[i + j + 1] == s2[j]) and poss[j]) or
                       ((s3[i + j + 1] == s1[i]) and poss[j + 1]));
      }
    }
    return poss[N];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
