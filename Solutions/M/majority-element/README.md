# Majority element

[Problem link](https://leetcode.com/problems/majority-element)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/majority-element

class Solution {
 public:
  int majorityElement(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    return nums[nums.size() / 2];
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, best = 0, 0
        for x in nums:
            if cnt == 0:
                cnt, best = 1, x
            else:
                cnt += 1 if x == best else -1
        return best
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Majority element](/Collections/majority-element.md#majority-element)
