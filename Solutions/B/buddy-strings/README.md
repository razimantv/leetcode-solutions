# Buddy strings

[Problem link](https://leetcode.com/problems/buddy-strings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/buddy-strings

class Solution {
 public:
  bool buddyStrings(string A, string B) {
    int N = A.size();
    if (N != B.size()) return false;

    bool two{};
    vector<int> cnt(26), bad;
    for (int i = 0; i < N; ++i) {
      if (A[i] == B[i]) {
        if (++cnt[A[i] - 'a'] > 1) two = true;
      } else {
        bad.push_back(i);
        if (bad.size() > 2) return false;
      }
    }
    return (bad.empty() and two) or
           (bad.size() == 2 and A[bad[0]] == B[bad[1]] and
            A[bad[1]] == B[bad[0]]);
  }
};
```