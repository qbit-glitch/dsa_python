from itertools import combinations

def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum_hashing([-1, 0, 1, 2, -1, -4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> find_triplets_with_0_sum_hashing([])
        []
        >>> find_triplets_with_0_sum_hashing([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum_hashing([1, 2, 3, 0, -1, -2, -3])
        [[-1, 0, 1], [-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3]]

    """    
    return [
        list(x)
        for x in sorted({i for i in combinations(sorted(nums),3) if not sum(i)})
    ]

def find_triplets_with_0_sum_hashing(nums: list[int]) -> list[list[int]]:
    """
    Function for finding the triplets with a given sum in the array using hashing
    Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum_hashing([-1, 0, 1, 2, -1, -4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> find_triplets_with_0_sum_hashing([])
        []
        >>> find_triplets_with_0_sum_hashing([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum_hashing([1, 2, 3, 0, -1, -2, -3])
        [[-1, 0, 1], [-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3]]

        Time Complexity: O(n^2)
        Auxillary Space: O(n)
    """
    target_sum = 0
    output_arr = []

    for i, v1 in enumerate(nums[:-2]):
        current_sum = target_sum - v1
        hash_set = set()

        for v2 in nums[i+1:]:
            required_sum = current_sum - v2
            if required_sum in hash_set:
                # triplet found. sort the triplet
                triplet = sorted([v1, v2, required_sum])
                if triplet not in output_arr:
                    output_arr.append(triplet)

            # include the current element in the set
            # for subsequent complement verification
            hash_set.add(v2)
    
    # return all triplet combinations
    return output_arr


if __name__ == "__main__":
    import doctest

    nums = [1,2,4,-1,0,-2,3,5]
    print(find_triplets_with_0_sum(nums))
    print("-----------------------------------------")
    print(find_triplets_with_0_sum_hashing(nums))

    doctest.testmod()

