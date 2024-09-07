# Shuffle an array

[Problem link](https://leetcode.com/problems/shuffle-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shuffle-an-array

class Solution {
 public:
  vector<int> v;
  Solution(vector<int>& nums) : v(nums) {}

  /** Resets the array to its original configuration and return it. */
  vector<int> reset() { return v; }

  /** Returns a random shuffling of the array. */
  vector<int> shuffle() {
    auto ret = v;
    random_shuffle(ret.begin(), ret.end());
    return ret;
  }
};

```