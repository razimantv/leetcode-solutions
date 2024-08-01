# Maximum units on a truck

[Problem link](https://leetcode.com/problems/maximum-units-on-a-truck)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-units-on-a-truck

class Solution {
 public:
  int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
    int B = boxTypes.size();
    sort(boxTypes.begin(), boxTypes.end(),
         [](const vector<int>& b1, const vector<int>& b2) {
           return b1[1] > b2[1];
         });

    int ret = 0;
    for (int i = 0; i < B and truckSize > 0; ++i) {
      ret += boxTypes[i][1] * min(truckSize, boxTypes[i][0]);
      truckSize -= boxTypes[i][0];
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Greedy](/Collections/greedy.md#greedy)
