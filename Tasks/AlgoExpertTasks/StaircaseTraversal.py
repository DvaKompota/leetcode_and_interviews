# Consider the staircase. You can take 1 step or 2 steps at a time
# How many ways can you reach to the top
#
#                         +----
#                         |4
#                    +----+
#                    |3
#               +----+
#               |2
#          +----+
#          |1                            N = 4
#      ----+
#        0
#
#
#          +----+                      N = 1
#          |1                          1 way to reach to the top
#      ----+                           {0, 1}
#        0
#
#               +----+
#               |2
#          +----+                      N = 2
#          |1                          2 ways to reach to the top
#      ----+                           {0, 1, 2} or {0, 2}
#        0


def staircase_traversal_recursive_memoization(height, max_steps):
    """
    You're given two positive integers representing the height of a staircase and the maximum number of steps that you
    can advance up the staircase at a time.
    Write a function that returns the number of ways in which you can climb the staircase.

    For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways.
    You could take 1 step, 1 step, then 1 step, you could also take 1 step, then 2 steps, and you could take 2 steps,
    then 1 step.

    Note that max_steps <= height will always be true.

    Input: two integers height, max_steps
    Output: an integer of the number of ways in which you can climb the staircase

    Examples:
        1. Given height = 3, max_steps = 2, the function should return 3.
            You can climb the staircase in 3 different ways:
                take 1 step, 1 step, then 1 step;
                take 1 step, then 2 steps;
                take 2 steps, then 1 step.
        2. Given height = 4, max_steps = 2, the function should return 5.
            You can climb the staircase in the following ways:
                1, 1, 1, 1
                1, 1, 2
                1, 2, 1
                2, 1, 1
                2, 2
    """
    memo = {0: 1, 1: 1}

    def _staircase_traversal_recursive_memoization(_height, _max_steps, _memo):
        if _height in _memo:
            return _memo[_height]

        answer = 0
        for step in range(1, min(_max_steps, _height) + 1):
            answer += _staircase_traversal_recursive_memoization(_height - step, _max_steps, _memo)
        _memo[_height] = answer
        return answer

    return _staircase_traversal_recursive_memoization(height, max_steps, memo)


def staircase_traversal_iterative_nested_sum(height, max_steps):
    step_count = [0] * (height + 1)
    step_count[0:2] = [1, 1]

    for current_height in range(2, height + 1):
        step = 1
        while step <= max_steps and step <= current_height:
            step_count[current_height] += step_count[current_height - step]
            step += 1

    return step_count[height]


def staircase_traversal_iterative_remove_add(height, max_steps):
    step_count = [1, 1]
    current_step_count = step_count[-1]

    for currentHeight in range(2, height + 1):
        step_to_remove = currentHeight - max_steps - 1
        step_to_add = currentHeight - 1
        if step_to_remove >= 0:
            current_step_count -= step_count[step_to_remove]
        current_step_count += step_count[step_to_add]
        step_count.append(current_step_count)

    return step_count[height]
