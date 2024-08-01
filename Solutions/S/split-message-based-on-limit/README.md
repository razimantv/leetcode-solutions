# Split message based on limit

[Problem link](https://leetcode.com/problems/split-message-based-on-limit/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/split-message-based-on-limit/

class Solution {
 public:
  int cnt(int limit, int n) {
    int ret{};
    auto s = to_string(n);
    for (int start = 1, end = 9, x = limit - 4 - s.size(); x > 0 and start <= n;
         start = end + 1, end = end * 10 + 9, --x) {
      ret += x * (min(end, n) - start + 1);
    }
    return ret;
  }
  vector<string> splitMessage(string message, int limit) {
    int L = message.size();
    int n = -1;
    for (int i = 1; i <= L; ++i)
      if (cnt(limit, i) >= L) {
        n = i;
        break;
      }
    if (n == -1) return {};
    vector<string> ret;
    for (int i = 1, pos = 0; i <= n; ++i) {
      string suffix = "<" + to_string(i) + "/" + to_string(n) + ">";
      int len = min(L - pos, limit - (int)suffix.size());
      ret.push_back(message.substr(pos, len) + suffix);
      pos += len;
    }
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
