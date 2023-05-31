# Calculate delayed arrival time

[Problem link](https://leetcode.com/problems/calculate-delayed-arrival-time/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution {
 public:
  int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    return (arrivalTime + delayedTime) % 24;
  }
};
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
