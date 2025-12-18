# Best time to buy and sell stock using strategy

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        tot, k = sum(x * y for x, y in zip(prices, strategy)), k // 2
        cur = sum(
            x * ((0 if i < k else 1) - y)
            for i, (x, y) in enumerate(islice(zip(prices, strategy), 2 * k))
        )
        ret = max(tot, cur + tot)
        for i in range(2 * k, len(prices)):
            cur += (
                prices[i] * (1 - strategy[i]) - prices[i - k] +
                prices[i - 2 * k] * strategy[i - 2 * k]
            )
            ret = max(ret, cur + tot)
        return ret
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
