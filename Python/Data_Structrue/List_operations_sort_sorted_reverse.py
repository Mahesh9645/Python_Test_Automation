# list_operations.py

# -------------------------
# sort vs sorted
# -------------------------

# Using sort() - modifies the original list
my_list = [3, 1, 4, 1, 5]
print("Original list (before sort()):", my_list)

my_list.sort()  # Sorts the list in place
print("List after sort():", my_list)

# Using sorted() - creates a new sorted list without modifying the original
another_list = [3, 1, 4, 1, 5]
print("\nOriginal list (before sorted()):", another_list)

new_sorted_list = sorted(another_list)  # Returns a new sorted list
print("New sorted list:", new_sorted_list)
print("Original list remains unchanged:", another_list)

# -------------------------
# reverse vs reversed
# -------------------------

# Using reverse() - modifies the original list in place
my_list = [1, 2, 3, 4, 5]
print("\nOriginal list:", my_list)

my_list.reverse()  # Reverses the list in place
print("List after reverse():", my_list)

# Using reversed() - returns an iterator, original list remains unchanged
another_list = [1, 2, 3, 4, 5]
print("\nOriginal list:", another_list)

reversed_list = list(reversed(another_list))  # Convert iterator to list
print("Reversed list using reversed():", reversed_list)
print("Original list remains unchanged:", another_list)

# -------------------------
# Sorting in Reverse Order
# -------------------------

# Using sort() with reverse=True - modifies the list in place
list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list1.sort(reverse=True)  # Sorts in reverse (descending) order
print("\nList after sorting in reverse order:", list1)

# Using sort() with reverse=True and capturing the result
list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list2 = list1.sort(reverse=True)  # Returns None, modifies list1 in place
print("list2 after sorting (should be None):", list2)
print("Original list1 after sorting:", list1)

# -------------------------
# Notes:
# 1. sort():
# - Modifies the list in place (does not return a new list).
# - Works only on lists.
# - Can sort in reverse order using reverse=True.
#
# 2. sorted():
# - Returns a new sorted list, does not modify the original list.
# - Works with any iterable (lists, tuples, dictionaries, sets, etc.).
#
# 3. reverse():
# - Reverses the list in place (modifies the original list).
# - Works only on lists.
#
# 4. reversed():
# - Returns an iterator (does not modify the original list).
# - Works with any iterable (lists, tuples, strings, etc.).
# -------------------------
