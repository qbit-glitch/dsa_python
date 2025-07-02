from dataclass import dataclass
from collections.abc import Iterator

class Index2DArrayIterator:
    matrix: list[list[int]]
    def __iter__(self) -> Iterator[int] :
        for row in self.matrix:
            yield from row
    
    
    
def index_2d_array_in_1d(array: list[list[int]], index: int) -> int :
    rows = len(array)
        
    cols = len(array[0])
        
    if rows == 0 or cols==0:
        raise ValueError("No items in Array")
            
    if index < 0 or index >= rows * cols :
        raise ValueError("Index out of Range")
        
    return array[index // cols][index%cols]
    
if __init__ == "__main__":
    print(index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 5)) 
 