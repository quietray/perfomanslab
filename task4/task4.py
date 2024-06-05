import sys
import numpy as np

def min_moves_to_equal(nums):
    median = int(np.median(nums))
    return sum(abs(num - median) for num in nums)

if name == "__main__":
    if len(sys.argv) != 2:
        print("incorrect input")
        sys.exit(1)

    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as file:
            nums = [int(num) for line in file for num in line.split()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    result = min_moves_to_equal(nums)
    print(result)
