#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = []   # Stack for incoming elements
        self.stack_out = []  # Stack for outgoing elements

    def push(self, x: int) -> None:
        """Push element x to the back of the queue."""
        self.stack_in.append(x)

    def pop(self) -> int:
        """Removes the element from the front of the queue and returns it."""
        self.move_in_to_out()  # Ensure stack_out has the current front
        return self.stack_out.pop()

    def peek(self) -> int:
        """Get the front element of the queue."""
        self.move_in_to_out()  # Ensure stack_out has the current front
        return self.stack_out[-1]

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        return not self.stack_in and not self.stack_out

    def move_in_to_out(self) -> None:
        """Transfer elements from stack_in to stack_out if stack_out is empty."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

