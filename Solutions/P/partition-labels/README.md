# Partition labels

[Problem link](https://leetcode.com/problems/partition-labels)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partition-labels

class Solution {
 public:
  vector<int> partitionLabels(string S) {
    int last[26];
    for (int i = 0; i < S.size(); ++i) last[S[i] - 'a'] = i;

    vector<int> ret;
    for (int i = 0, j = 0; i < S.size(); i = ++j) {
      for (int k = i; k <= j; ++k) j = max(j, last[S[k] - 'a']);
      ret.push_back(j - i + 1);
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap)
