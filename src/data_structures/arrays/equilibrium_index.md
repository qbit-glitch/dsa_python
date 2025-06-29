# Equilibrium Index in Arrays

```python
def equilibrium_index(arr: list[int]) -> int :
    total_sum = sum(arr)
    left_sum = 0

    for i, v in enumerate(arr):
        total_sum -= v
        if total_sum == left_sum:
            return i
        left_sum += v
    return -1

if __name__ == "__main__":
    nums = [8,6,2,0,1,2,8,6]
    print(equilibrium_index(nums))
```
    