# H index

[Problem link](https://leetcode.com/problems/h-index)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/h-index

class Solution {
 public:
  int hIndex(vector<int>& citations) {
    int start = 0, end = citations.size() + 1;
    while (end - start > 1) {
      int mid = (start + end) / 2, cnt = 0;
      for (int c : citations)
        if (c >= mid and ++cnt == mid) break;
      (cnt == mid ? start : end) = mid;
    }
    return start;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
