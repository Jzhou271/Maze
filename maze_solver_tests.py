"""
Maze Solver -- test file of Maze Solover
To test functions are not required keyboard input, to check if its expected
outputs are the same as actual outputs.
"""
import maze_solver


def test_check_maze():
    """
    This is the test function to test check_maze() in file maze-file.py.
    it takes a list of string of 'X', 'E', and ' ' as input test parameter,
    defined as variable "test_maze", get output of True or False to check if
    its expected outputs are the same as actual outputs.
    """
    test_maze = ["XXX", "XQX", "XXX"]
    actual = maze_solver.check_maze(test_maze)
    expected = False
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")

    test_maze = ["XXXXX", "XX  X", "X   X", "X   X", "XXXXX"]
    actual = maze_solver.check_maze(test_maze)
    expected = False
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")


def test_get_neighbors():
    """
    This is the test function to test get_neighbors() in file maze-file.py.
    it takes a tuple of int as input test parameter, defined as variable
    "test_point", get output of list of tuples to check if its expected
    outputs are the same as actual outputs.
    """
    test_point = (2, 3)
    actual = maze_solver.get_neighbors(test_point)
    expected = [(3, 3), (2, 4), (1, 3), (2, 2)]
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")

    test_point = (5, 2)
    actual = maze_solver.get_neighbors(test_point)
    expected = [(6, 2), (5, 3), (4, 2), (5, 1)]
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")


def test_find_exits():
    """
    This is the test function to test find_exits() in file maze-file.py.
    it takes a list of string of 'X', 'E', and ' ' as first input test
    parameter, starting point of maze as the second input test parameter, which
    defined as variable 'test_maze' and 'test_start'. To get output of empty
    list to check if its expected outputs are the same as actual outputs.
    """
    test_maze = ["XXX", "X X", "XEX"]
    test_start = (1, 1)
    actual = maze_solver.find_exits(test_maze, test_start)
    expected = []
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")

    test_maze = ["XXXX", "X XX", "XXEX"]
    test_start = (1, 1)
    actual = maze_solver.find_exits(test_maze, test_start)
    expected = []
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")


def test_get_next_location():
    """
    This is the test function to test get_next_location() in file maze-file.py.
    it takes a tuple of current location as the first input test parameters,
    and an int as the second test parameter, defined as variable 'test_maze'
    and 'test_start', to get output of empty list and check if its expected
    outputs are the same as actual outputs.
    """
    test_current = (2, 2)
    test_direction_int = 2
    actual = maze_solver.get_next_location(test_current, test_direction_int)
    expected = (3, 2)
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")

    test_current = (6, 3)
    test_direction_int = 4
    actual = maze_solver.get_next_location(test_current, test_direction_int)
    expected = (6, 4)
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")
    

def test_get_path_to_exit():
    """
    This is the test function to test get_path_to_exit() in file maze-file.py.
    it takes a list of string of 'X', 'E', and ' ' as first input test
    parameter, a tuple of starting point as the second input test parameters,
    and a tuple of ending point as the second input test parameters, defined
    as variable 'test_maze', 'test_start', and 'test_exit'. finally check if
    its expected outputs are the same as actual outputs.
    """
    test_maze = ["XXXX", "X  X", "X  X", "XXEX"]
    test_start = (1, 1)
    test_exit = (2, 2)
    actual = maze_solver.get_path_to_exit(test_maze, test_start, test_exit)
    expected = [(1, 1)]
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")

    test_maze = ["XXX", "X X", "X X", "X X" "XEX"]
    test_start = (1, 1)
    test_exit = (3, 1)
    actual = maze_solver.get_path_to_exit(test_maze, test_start, test_exit)
    expected = [(1, 1)]
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")


def footprint():
    test_maze = ['XXXX', 'X  X', 'X  X', 'XXEX']
    actual = maze_solver.footprint(test_maze)
    print(actual)
    # enter x coordinate = 1 and y coordinate = 1
    expected = [(3, 2), (2, 2), (2, 1), (1, 1)]
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected output is", expected)
        print("Actual output is", actual)
    else:
        print("PASSED ON THE TEST")


def main():
    test_check_maze()
    test_get_neighbors()
    test_find_exits()
    test_get_next_location()
    test_get_path_to_exit()
    footprint()


if __name__ == '__main__':
    main()
