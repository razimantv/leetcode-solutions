# The latest time to catch a bus

[Problem link](https://leetcode.com/problems/the-latest-time-to-catch-a-bus)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus

class Solution {
 public:
  bool poss(vector<int>& buses, vector<int>& passengers, int capacity, int t) {
    for (int i = 0, j = 0, cur = 0; i < buses.size();) {
      if (t == passengers[j]) {
        ++t;
        continue;
      } else if (buses[i] < min(passengers[j], t)) {
        ++i;
        cur = 0;
        continue;
      } else if (t < passengers[j])
        return true;
      else {
        ++j;
        if (++cur == capacity) cur = 0, ++i;
      }
    }
    return false;
  }
  int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers,
                            int capacity) {
    sort(buses.begin(), buses.end());
    sort(passengers.begin(), passengers.end());
    passengers.push_back(INT_MAX);
    int start = 1, end = buses.back() + 1;
    while (end - start > 1) {
      int mid = (start + end) >> 1;
      (poss(buses, passengers, capacity, mid) ? start : end) = mid;
    }
    return start;
  }
};
```