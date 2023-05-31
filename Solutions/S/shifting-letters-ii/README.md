# Shifting letters ii

[Problem link](https://leetcode.com/problems/shifting-letters-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shifting-letters-ii

class Solution {
 public:
  string shiftingLetters(string s, vector<vector<int>>& shifts) {
    int n = s.size();
    vector<int> add(n + 1);
    for (auto& v : shifts) {
      int l = v[0], r = v[1] + 1, d = v[2] ? 1 : 25;
      add[l] = (add[l] + d) % 26;
      add[r] = (add[r] + 26 - d) % 26;
    }

    for (int i = 0, pref = 0; i < n; ++i) {
      pref = (pref + add[i]) % 26;
      s[i] = 'a' + (s[i] - 'a' + pref) % 26;
    }
    return s;
  }
};
```