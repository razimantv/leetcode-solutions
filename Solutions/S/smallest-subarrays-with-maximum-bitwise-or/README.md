# Smallest subarrays with maximum bitwise or

[Problem link](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution {
 public:
  vector<int> smallestSubarrays(vector<int>& nums) {
    vector<int> last(30);
    int n = nums.size();
    vector<int> answer(n);

    for (int i = n - 1; i >= 0; --i) {
      for (int j = 0; j < 30; ++j)
        if (nums[i] & (1 << j)) last[j] = i;

      answer[i] = max(1, *max_element(last.begin(), last.end()) - i + 1);
    }
    return answer;
  }
};
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Right to left](/README.md#Array_scanning-Right_to_left)
* [Hashmap](/README.md#Hashmap)
* [Bitwise operation](/README.md#Bitwise_operation)
