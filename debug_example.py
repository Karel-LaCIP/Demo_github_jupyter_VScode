import numpy as np
def debug_example():
    # Create a sample array
    arr = np.array([1, 2, 3, 4, 5])
    
    # Print the original array
    print("Original array:", arr)
    
    # Perform a simple operation: square each element
    squared_arr = arr ** 2
    
    # Print the squared array
    print("Squared array:", squared_arr)

    to_list = squared_arr.tolist()
    # Print the list version of the squared array
    print("List version of squared array:", to_list)

    squared_list = to_list**2

    # Print the squared array
    print("Squared list:", squared_list)


if __name__ == "__main__":
    debug_example()