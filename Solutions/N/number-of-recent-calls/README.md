# Number of recent calls

[Problem link](https://leetcode.com/problems/number-of-recent-calls)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-recent-calls

class RecentCounter {
  queue<int> q;

 public:
  RecentCounter() {}

  int ping(int t) {
    q.push(t);
    while (!q.empty()) {
      int f = q.front();
      if (t - f > 3000)
        q.pop();
      else
        break;
    }
    return q.size();
  }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
```
## Tags

* [Queue](/README.md#Queue)
* [Design data structure](/README.md#Design_data_structure)
