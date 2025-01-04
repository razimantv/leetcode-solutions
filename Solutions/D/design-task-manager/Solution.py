# https://leetcode.com/problems/design-task-manager

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self. data, self. todo = {}, SortedList()
        for user, task, priority in tasks:
            self.add(user, task, priority)

    def add(self, user: int, task: int, priority: int) -> None:
        self.data[task] = [user, priority]
        self.todo.add((-priority, -task, user))

    def edit(self, task: int, newPriority: int) -> None:
        user = self.data[task][0]
        self.rmv(task)
        self.add(user, task, newPriority)

    def rmv(self, task: int) -> None:
        user, priority = self.data[task]
        self.todo.remove((-priority, -task, user))
        del (self.data[task])

    def execTop(self) -> int:
        if not self.todo:
            return -1
        ret = self.todo[0][2]
        self.rmv(-self.todo[0][1])
        return ret
