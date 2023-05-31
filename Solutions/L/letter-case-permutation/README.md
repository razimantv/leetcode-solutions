# Letter case permutation

[Problem link](https://leetcode.com/problems/letter-case-permutation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/letter-case-permutation

class Solution {
 public:
  vector<string> letterCasePermutation(string S) {
    vector<string> ret{""};
    for (char c : S) {
      if (isdigit(c))
        for (auto& s : ret) s += c;
      else {
        int N = ret.size();
        for (int i = 0; i < N; ++i) {
          ret.push_back(ret[i]);
          ret.back() += toupper(c);
          ret[i] += tolower(c);
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Brute force enumeration](/README.md#Brute_force_enumeration) > [Elementwise processing using a vector](/README.md#Brute_force_enumeration-Elementwise_processing_using_a_vector)
