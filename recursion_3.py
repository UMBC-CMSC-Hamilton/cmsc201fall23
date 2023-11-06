"""
    Recursion today
"""


def a_and_b(n, k, current):
    if n == 0:
        print(current)
        return
    
    a_and_b(n - 1, current + 'a')
    a_and_b(n - 1, current + 'b')


# a_and_b(4, 0, '')


"""
    Pathfinding example: project 3 - recursion project
        family trees, phone networks, internet, kinda stuff
        
    Let's say that I have a grid:
    
    S _ _ _ * * * _ _ _ _
    _ _ _ _ _ _ _ _ _ _ _
    * * * _ _ * _ _ _ * *
    _ _ _ _ * E _ _ * * _
"""

import random

WALL = "*"
BLANK = "_"
THE_END = 'E'


def make_grid(height, width, prob):
    new_grid = []
    for i in range(height):
        new_row = []
        for j in range(width):
            if random.random() < prob:
                new_row.append(WALL)
            else:
                new_row.append(BLANK)
        new_grid.append(new_row)
    
    ending_row = random.randint(0, height - 1)
    ending_col = random.randint(0, width - 1)
    new_grid[ending_row][ending_col] = THE_END
    return new_grid


def display_grid(the_grid):
    for row in the_grid:
        print(" ".join(row))


def pathfinding(the_grid, current_pos, visited):
    x, y = current_pos
    if the_grid[x][y] == THE_END:
        return [current_pos]
    """
        Either you go up, down, left, right
            go all the directions that we can
        We have to check that we're on the board
        We should check at some point that we're not hitting a wall
    """
    if (x, y) in visited:
        return []  # we didn't find a path
    # print(current_pos)
    the_grid[x][y] = 'b'
    visited.append((x, y))
    
    # up = (x - 1, y)
    if 0 <= x - 1 < len(the_grid) and the_grid[x - 1][y] != WALL:
        path = pathfinding(the_grid, (x - 1, y), visited)
        if path:
            the_grid[x][y] = '^'
            path = [current_pos] + path
            return path
    # down = (x + 1, y)
    if 0 <= x + 1 < len(the_grid) and the_grid[x + 1][y] != WALL:
        path = pathfinding(the_grid, (x + 1, y), visited)
        if path:
            the_grid[x][y] = 'v'
            path = [current_pos] + path
            return path
    # left = (x, y - 1)
    if 0 <= y - 1 < len(the_grid[x]) and the_grid[x][y - 1] != WALL:
        path = pathfinding(the_grid, (x, y - 1), visited)
        if path:
            the_grid[x][y] = '<'
            path = [current_pos] + path
            return path
    # right = (x, y + 1)
    if 0 <= y + 1 < len(the_grid[x]) and the_grid[x][y + 1] != WALL:
        path = pathfinding(the_grid, (x, y + 1), visited)
        if path:
            path = [current_pos] + path
            the_grid[x][y] = '>'
            return path
    
    return []


the_grid = make_grid(10, 10, 0.2)
display_grid(the_grid)
print(pathfinding(the_grid, (0, 0), []))
display_grid(the_grid)

"""
_ _ E _ _ _ _ _ _ _
_ * _ * _ _ _ _ _ _
_ _ _ _ * _ * * _ _
_ _ _ _ * _ _ _ _ *
_ _ _ * _ _ _ _ _ _
* _ _ _ * _ * _ _ _
_ * * _ _ _ _ _ _ _
_ _ * _ _ _ * _ * _
* _ _ _ _ _ * _ _ _
_ _ _ _ * * _ * _ _
(0, 0)
(1, 0)
(2, 0)
(3, 0)
(4, 0)
(4, 1)
(3, 1)
(2, 1)
(2, 2)
(1, 2)
(0, 2)
p _ E _ _ _ _ _ _ _
p * p * _ _ _ _ _ _
p p p _ * _ * * _ _
p p _ _ * _ _ _ _ *
p p _ * _ _ _ _ _ _
* _ _ _ * _ * _ _ _
_ * * _ _ _ _ _ _ _
_ _ * _ _ _ * _ * _
* _ _ _ _ _ * _ _ _
_ _ _ _ * * _ * _ _


instead of four different if statements:
    use a loop
    number of connections can be different that's totally ok
    still need a visited list - infinite recursion
    
"""