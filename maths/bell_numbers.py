"""
Bell Numbers

Bell numbers count the number of ways to partition a set of n elements.
The nth Bell number is the number of partitions of a set with n members.

For example, B(3) = 5 because the 3-element set {1, 2, 3} can be partitioned
in 5 distinct ways:
    {{1}, {2}, {3}}
    {{1, 2}, {3}}
    {{1, 3}, {2}}
    {{1}, {2, 3}}
    {{1, 2, 3}}

The Bell numbers can be calculated using the Bell triangle (similar to Pascal's
triangle) or using Dobinski's formula.

Reference: https://en.wikipedia.org/wiki/Bell_number
"""


def bell_number(n: int) -> int:
    """
    Calculate the nth Bell number using the Bell triangle method.

    The Bell triangle is constructed similar to Pascal's triangle:
    - First element of each row is the last element of the previous row
    - Each subsequent element is the sum of the element to its left and
      the element above the element to its left

    Args:
        n: A non-negative integer representing the position in the sequence

    Returns:
        The nth Bell number

    Raises:
        ValueError: If n is negative or not an integer

    Examples:
    >>> bell_number(0)
    1
    >>> bell_number(1)
    1
    >>> bell_number(2)
    2
    >>> bell_number(3)
    5
    >>> bell_number(4)
    15
    >>> bell_number(5)
    52
    >>> bell_number(10)
    115975
    >>> bell_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    >>> bell_number(2.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 1

    # Create the Bell triangle
    bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    bell[0][0] = 1

    for i in range(1, n + 1):
        # First element in row is last element of previous row
        bell[i][0] = bell[i - 1][i - 1]

        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

    return bell[n][0]


def bell_number_sum(n: int) -> int:
    """
    Calculate the nth Bell number using Stirling numbers of the second kind.

    Bell number B(n) = sum of S(n, k) for k = 0 to n,
    where S(n, k) is the Stirling number of the second kind.

    Args:
        n: A non-negative integer representing the position in the sequence

    Returns:
        The nth Bell number

    Raises:
        ValueError: If n is negative or not an integer

    Examples:
    >>> bell_number_sum(0)
    1
    >>> bell_number_sum(1)
    1
    >>> bell_number_sum(2)
    2
    >>> bell_number_sum(3)
    5
    >>> bell_number_sum(4)
    15
    >>> bell_number_sum(5)
    52
    >>> bell_number_sum(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 1

    # Calculate Stirling numbers using dynamic programming
    stirling = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        stirling[i][0] = 0
        stirling[0][i] = 0
    stirling[0][0] = 1

    # Fill the table using recurrence relation:
    # S(n, k) = k * S(n-1, k) + S(n-1, k-1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            stirling[i][j] = j * stirling[i - 1][j] + stirling[i - 1][j - 1]

    # Sum all Stirling numbers S(n, k) for k = 0 to n
    return sum(stirling[n])


def bell_numbers_list(n: int) -> list[int]:
    """
    Generate a list of the first n+1 Bell numbers (from B(0) to B(n)).

    Args:
        n: A non-negative integer

    Returns:
        A list containing Bell numbers from B(0) to B(n)

    Raises:
        ValueError: If n is negative or not an integer

    Examples:
    >>> bell_numbers_list(0)
    [1]
    >>> bell_numbers_list(5)
    [1, 1, 2, 5, 15, 52]
    >>> bell_numbers_list(7)
    [1, 1, 2, 5, 15, 52, 203, 877]
    >>> bell_numbers_list(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return [1]

    bell_list = [1]  # B(0) = 1
    for i in range(1, n + 1):
        bell_list.append(bell_number(i))

    return bell_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Print first 10 Bell numbers
    print("First 10 Bell numbers:")
    for i in range(10):
        print(f"B({i}) = {bell_number(i)}")

    print("\nBell triangle (first 6 rows):")
    for i in range(6):
        row = []
        for j in range(i + 1):
            # Reconstruct the triangle for display
            bell = [[0 for _ in range(i + 1)] for _ in range(i + 1)]
            bell[0][0] = 1
            for x in range(1, i + 1):
                bell[x][0] = bell[x - 1][x - 1]
                for y in range(1, x + 1):
                    bell[x][y] = bell[x - 1][y - 1] + bell[x][y - 1]
            row.append(str(bell[i][j]))
        print(" ".join(row))
