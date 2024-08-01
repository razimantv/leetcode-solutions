# H index ii

[Problem link](https://leetcode.com/problems/h-index-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/h-index-ii

class Solution {
 public:
  int hIndex(vector<int>& citations) {
    if (citations.empty() or citations.back() == 0) return 0;

    int N = citations.size(), start = 0, end = N + 1;
    // invariant: start <= H < end
    while (end - start > 1) {
      int mid = (end + start) >> 1;
      if (citations[N - mid] >= mid)
        start = mid;
      else
        end = mid;
    }
    return start;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
