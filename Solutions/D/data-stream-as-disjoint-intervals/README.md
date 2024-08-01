# Data stream as disjoint intervals

[Problem link](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

class SummaryRanges {
 public:
  vector<vector<int>> ranges;
  SummaryRanges() {}

  void addNum(int value) {
    vector<int> temp{value, value};

    auto vit = upper_bound(ranges.begin(), ranges.end(), temp);
    bool flag{};
    if (vit != ranges.end() and (*vit)[0] <= value + 1) {
      (*vit)[0] = value;
      flag = true;
    }

    if (vit != ranges.begin()) {
      auto vit2 = vit;
      --vit2;
      if ((*vit2)[1] == value - 1) {
        (*vit2)[1] = value;
        flag = true;
      } else if ((*vit2)[1] >= value)
        flag = true;
      if (vit != ranges.end() and (*vit2)[1] >= (*vit)[0] - 1) {
        (*vit2)[1] = (*vit)[1];
        ranges.erase(vit);
      }
    }

    if (!flag) ranges.insert(vit, temp);
  }

  vector<vector<int>> getIntervals() { return ranges; }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Intervals](/Collections/intervals.md#intervals) > [Union](/Collections/intervals.md#union)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
