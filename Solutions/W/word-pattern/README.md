# Word pattern

[Problem link](https://leetcode.com/problems/word-pattern)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-pattern

class Solution {
 public:
  bool wordPattern(string pattern, string str) {
    string fw[26];
    unordered_map<string, char> bw;

    istringstream iss(str);
    string s;
    int p;
    char c;
    while (iss >> s) {
      if (p == pattern.size()) return false;
      c = pattern[p++] - 'a';
      if ((fw[c] != "" and fw[c] != s) or (bw.count(s) and bw[s] != c))
        return false;
      fw[c] = s;
      bw[s] = c;
    }
    return p == pattern.size();
  }
};
```