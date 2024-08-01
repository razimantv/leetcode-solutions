# Decode string

[Problem link](https://leetcode.com/problems/decode-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/decode-string

class Solution {
 public:
  pair<string, int> work(const string& s, int i, int N) {
    string ret;
    for (; i < N and s[i] != ']'; ++i) {
      if (isdigit(s[i])) {
        int k = 0;
        do {
          k = k * 10 + s[i] - '0';
        } while (isdigit(s[++i]));
        auto sub = work(s, i + 1, N);
        for (int j = 0; j < k; ++j) ret += sub.first;
        i = sub.second;
      } else
        ret += s[i];
    }
    return {ret, i};
  }
  string decodeString(string s) { return work(s, 0, s.size()).first; }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing) > [Recursive](/Collections/string.md#recursive)
