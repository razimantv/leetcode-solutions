# Maximal score after applying k operations

[Problem link](https://leetcode.com/problems/maximal-score-after-applying-k-operations/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution {
 public:
  long long maxKelements(vector<int>& nums, int k) {
    multiset<int, greater<int>> ms;
    for (int x : nums) ms.insert(x);
    long long ret{};
    for (int i = 0; i < k; ++i) {
      int u = *ms.begin();
      ms.erase(ms.begin());
      ret += u;
      ms.insert((u + 2) / 3);
    }
    return ret;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
