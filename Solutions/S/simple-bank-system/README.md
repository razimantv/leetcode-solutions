# Simple bank system

[Problem link](https://leetcode.com/problems/simple-bank-system/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/simple-bank-system/

class Bank:

    def __init__(self, balance: list[int]):
        self.balance = [0] + balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            max(account1, account2) < len(self.balance) and
            self.balance[account1] >= money
        ):
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account1: int, money: int) -> bool:
        if account1 < len(self.balance):
            self.balance[account1] += money
            return True
        return False

    def withdraw(self, account1: int, money: int) -> bool:
        if account1 < len(self.balance) and self.balance[account1] >= money:
            self.balance[account1] -= money
            return True
        return False
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
