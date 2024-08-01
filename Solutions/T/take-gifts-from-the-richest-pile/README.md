# Take gifts from the richest pile

[Problem link](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution {
 public:
  long long pickGifts(vector<int>& gifts, int k) {
    multiset<int, greater<int>> pq;
    for (int x : gifts) pq.insert(x);
    for (int i = 0; i < k; ++i) {
      int x = *pq.begin();
      pq.erase(pq.begin());
      pq.insert(sqrt(x));
    }
    return accumulate(pq.begin(), pq.end(), 0ll);
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
