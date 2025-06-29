"""
Run the python doctest with the following command:
python -m doctest -v equilibrium_index_in_array.py
"""


def equilibrium_index(arr: list[int]) -> int :
    """
    Find the equilibrium index of an array
    Args:
        arr(list[int]): The input array of integers
    Returns:
        int: The equilibrium index or -1 if no equilibrium index exists.
    
    Examples:
        >>> equilibrium_index([-7,1,5,2,-4,3,0])
        3
        >>> equilibrium_index([1,2,3,4,5])
        -1
        >>> equilibrium_index([1,1,1,1,1])
        2
        >>> equilibrium_index([2,4,6,8,10,3])
        -1
    """
    total_sum = sum(arr)
    left_sum = 0

    for i, v in enumerate(arr):
        total_sum -= v
        if total_sum == left_sum:
            return i
        left_sum += v
    return -1

if __name__ == "__main__":
    import doctest
    nums = [8,6,2,0,1,2,8,6]
    print(equilibrium_index(nums))

    doctest.testmod()
    