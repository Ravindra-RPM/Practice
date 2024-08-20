# The map() function applies a given function to each item 
# in an iterable (like a list) and returns an iterable with the results.

# Example: Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# -----------------------------------------------------------------------

#  filter()
# The filter() function sifts through an iterable and returns
# only the items that meet a specified condition. 

# Example: Keeping only the odd numbers from a list
numbers = [1, 2, 3, 4, 5]
odd_numbers = list[filter(lambda x: x % 2 != 0, numbers)]