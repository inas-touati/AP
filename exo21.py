import math

def length(lst):
    """
    Returns the number of elements in the list.
    
    Args:
        lst (list): A list of numeric values.
    
    Returns:
        int: The number of elements in the list.
    
    Raises:
        ValueError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    return len(lst)


def mean(lst):
    """
    Calculates the arithmetic mean (average) of the numbers in the list.
    
    Args:
        lst (list): A list of numeric values.
    
    Returns:
        float: The mean of the list.
    
    Raises:
        ValueError: If the list is empty or contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("Cannot calculate the mean of an empty list.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements of the list must be numeric values.")
    
    return sum(lst) / len(lst)


def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    
    Args:
        lst (list): A list of numeric values.
    
    Returns:
        float: The range of the list (max - min).
    
    Raises:
        ValueError: If the list is empty or contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("Cannot calculate the range of an empty list.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements of the list must be numeric values.")
    
    return max(lst) - min(lst)


def median(lst):
    """
    Calculates the median of the list.
    
    Args:
        lst (list): A list of numeric values.
    
    Returns:
        float: The median of the list.
    
    Raises:
        ValueError: If the list is empty or contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("Cannot calculate the median of an empty list.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements of the list must be numeric values.")
    
    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    
    if n % 2 == 0:
        return (lst_sorted[n//2 - 1] + lst_sorted[n//2]) / 2
    else:
        return lst_sorted[n//2]


def standard_deviation(lst):
    """
    Calculates the standard deviation of the list.
    
    Args:
        lst (list): A list of numeric values.
    
    Returns:
        float: The standard deviation of the list.
    
    Raises:
        ValueError: If the list is empty or contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("Cannot calculate the standard deviation of an empty list.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements of the list must be numeric values.")
    
    mean_val = mean(lst)
    variance = sum((x - mean_val) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)


def list_statistics(lst):
    """
    Creates a dictionary with statistics about the list.
    
    Args:
        lst (list): A list of numeric values.
    
    Returns:
        dict: A dictionary with length, mean, range, median, and standard deviation.
    
    Raises:
        ValueError: If the list is empty or contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        raise ValueError("Cannot calculate statistics of an empty list.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements of the list must be numeric values.")
    
    stats = {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }
    
    return stats


# Sample test cases
numbers = [1, 2, 3, 4, 5]
print("List:", numbers)
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))
print("Median:", median(numbers))
print("Standard Deviation:", standard_deviation(numbers))
print("Statistics:", list_statistics(numbers))

print("\nEdge Cases:")
print("Empty List:", length([])) 
print("Single Element:", length([42])) 
print("List with Negative Numbers:", range_of_list([-5, -2, -10])) 
print("Floating-point List:", mean([1.5, 2.5, 3.5])) 
