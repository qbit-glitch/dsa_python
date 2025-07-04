# Permutations

Code:
```python
def permute_recursive(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations:

    >>> permute_recursive([1,2,3])
    [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
    """
    if len(nums) == 0 :
        return [[]]

    result: list[list[int]] = []
    
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute_recursive(nums)
        for perm in permutations:
            perm.append(n)
        
        result.extend(permutations)
        nums.append(n)

    return result

def permute_backtrack(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations of the given list.

    >>> permute_backtrack([1,2,3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """

    def backtrack(start: int) -> None:
        if start == len(nums) - 1 :
            output.append(nums[:])
        else :
            for i in range(start,  len(nums)):
                nums[start],  nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[i], nums[start] = nums[start], nums[i]
    
    output: list[list[int]] = []
    backtrack(0)
    return output

if __name__ == "__main__":
    import doctest

    nums = [1,2,3]
    result = permute_backtrack(nums)
    print(result)

    doctest.testmod()
```