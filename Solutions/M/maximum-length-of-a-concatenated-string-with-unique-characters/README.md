# Maximum length of a concatenated string with unique characters

[Problem link](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution {
 public:
  int maxLength(vector<string>& arr) {
    vector<int> masks;
    for (string& s : arr) {
      int x = 0;
      for (char c : s) {
        if (x & (1 << (c - 'a'))) goto BPP;
        x |= (1 << (c - 'a'));
      }
      masks.push_back(x);
      continue;
    BPP:;
      s.clear();
      masks.push_back(0);
    }

    int N = arr.size(), best = 0;
    for (int m = 1; m < (1 << N); ++m) {
      int cur = 0, pref = 0;
      for (int i = 0; i < N; ++i) {
        if (m & (1 << i)) {
          if (pref & masks[i]) goto BPP2;
          cur += arr[i].size();
          pref |= masks[i];
        }
      }
      best = max(best, cur);
    BPP2:;
    }
    return best;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
