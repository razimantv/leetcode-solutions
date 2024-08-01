# Minimum size subarray sum

[Problem link](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution {
 public:
  // ChatGPT solution
  int minSubArrayLen(int target, vector<int>& nums) {
    int left = 0, right = 0;
    int sum = 0;
    int minLength = std::numeric_limits<int>::max();

    while (right < nums.size()) {
      sum += nums[right];

      while (sum >= target) {
        minLength = std::min(minLength, right - left + 1);
        sum -= nums[left];
        left++;
      }

      right++;
    }

    return (minLength == std::numeric_limits<int>::max()) ? 0 : minLength;
  }
};
```
## Tags

* [ChatGPT](/Collections/chatgpt.md#chatgpt)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
