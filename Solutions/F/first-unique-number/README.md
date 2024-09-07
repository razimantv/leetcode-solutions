# First unique number

[Problem link](https://leetcode.com/problems/first-unique-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/first-unique-number

class FirstUnique {
 public:
  map<int, int> postoval, valtopos;
  int next = 0;
  FirstUnique(vector<int>& nums) {
    postoval.clear();
    valtopos.clear();
    next = 0;
    for (auto n : nums) {
      add(n);
    }
  }

  int showFirstUnique() {
    if (postoval.empty()) return -1;
    return postoval.begin()->second;
  }

  void add(int n) {
    if (valtopos.count(n)) {
      if (postoval.count(valtopos[n])) postoval.erase(valtopos[n]);
    } else {
      postoval[valtopos[n] = next++] = n;
    }
  }
};

```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
