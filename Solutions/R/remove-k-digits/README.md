# Remove k digits

[Problem link](https://leetcode.com/problems/remove-k-digits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-k-digits

class Solution {
 public:
  string removeKdigits(string num, int k) {
    string ret = "";
    int N = num.size(), req = N - k;
    for (int next = 0; req > 0 and next < num.size(); --req) {
      int bestpos = next;
      char best = num[next];
      for (int i = next + 1; i + req <= N; ++i) {
        if (num[i] < best) {
          best = num[i];
          bestpos = i;
        }
      }

      if (best > '0' or ret != "") ret += best;
      next = bestpos + 1;
    }

    if (ret == "") ret = "0";
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
