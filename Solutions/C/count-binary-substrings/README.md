# Count binary substrings

[Problem link](https://leetcode.com/problems/count-binary-substrings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-binary-substrings

class Solution {
 public:
  int countBinarySubstrings(string s) {
    char prev = '0';
    int cur = 0;
    vector<int> cnt;
    for (char c : s) {
      if (c != prev) {
        cnt.push_back(cur);
        cur = 1;
        prev = c;
      } else
        ++cur;
    }
    cnt.push_back(cur);

    int N = cnt.size(), ret = 0;
    for (int i = 1; i < N; ++i) ret += min(cnt[i], cnt[i - 1]);
    return ret;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
