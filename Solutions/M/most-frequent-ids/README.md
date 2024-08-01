# Most frequent ids

[Problem link](https://leetcode.com/problems/most-frequent-ids/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/most-frequent-ids/

class Solution {
 public:
  vector<long long> mostFrequentIDs(vector<int>& nums, vector<int>& freq) {
    unordered_map<int, long long> cnt;
    map<long long, int> invcnt;
    vector<long long> ret;
    int q = nums.size();
    for (int i = 0; i < q; ++i) {
      int x = nums[i];
      long long f = freq[i], f0 = cnt[x];
      if (f0 and !--invcnt[-f0]) invcnt.erase(-f0);
      ++invcnt[-(cnt[x] += f)];
      ret.push_back(-invcnt.begin()->first);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
