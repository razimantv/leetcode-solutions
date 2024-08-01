# Convert the temperature

[Problem link](https://leetcode.com/problems/convert-the-temperature/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/convert-the-temperature/

class Solution {
 public:
  vector<double> convertTemperature(double celsius) {
    return {celsius + 273.15, celsius * 1.8 + 32.};
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
