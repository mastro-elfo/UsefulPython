"""Utility class to solve a problem using backtrack algorithm.

Example
```py
class MyProblem(Backtrack):
    # Define the following methods as described: next, solved, candidates, valid, set, reset

MyProblem().solve(*args, **kwargs)
```

Example
```py
class MySolver(Backtrack):
    # Define the following methods as described: next, solved, candidates, valid, set, reset

MySolver().solve(a_problem)
```
"""


class Backtrack(object):
    def solve(self, *args, **kwargs):
        """Solve using backtrack recursive algorithm"""
        # Find the next item
        find = self.next(*args, **kwargs)
        if not find:
            # No next item, return if it's solved or not
            return self.solved(*args, **kwargs)
        # Get candidates
        for candidate in self.candidates(find, *args, **kwargs):
            if self.valid(candidate, find, *args, **kwargs):
                # If candidate is valid, set it
                self.set(candidate, find, *args, **kwargs)
                # Then call recursively
                if self.solve(*args, **kwargs):
                    # It's solved, return True
                    return True
                # It's not solve, reset and continue
                self.reset(find, *args, **kwargs)
        # Run out of candidates, it's unsolved (don't need to check)
        return False

    def set(self, candidate, find, *args, **kwargs):
        """Updates the state"""
        pass

    def reset(self, find, *args, **kwargs):
        """Resets the state"""
        pass

    def next(self, *args, **kwargs):
        """Returns the next item"""
        return None

    def candidates(self, find, *args, **kwargs):
        """Returns the list of candidates"""
        return []

    def valid(self, candidate, find, *args, **kwargs):
        """Returns True if the actual state is valid"""
        return False

    def solved(self, *args, **kwargs):
        """Returns True when problem is solved"""
        return False
