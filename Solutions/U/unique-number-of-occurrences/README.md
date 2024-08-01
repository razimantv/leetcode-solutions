# Unique number of occurrences

[Problem link](https://leetcode.com/problems/unique-number-of-occurrences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-number-of-occurrences

class Solution {
 public:
  bool uniqueOccurrences(vector<int>& arr) {
    unordered_map<int, int> cnt;
    for (int x : arr) ++cnt[x];

    unordered_set<int> seen;
    for (auto [k, v] : cnt)
      if (seen.count(v))
        return false;
      else
        seen.insert(v);

    return true;
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return max(Counter(Counter(arr).values()).values()) == 1
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
