arr = [0, 1, 2, 4, 5, 6, 7]  # 3 is missing
n = len(arr)  # Since the numbers are from 0 to n
total_sum = (n * (n + 1)) // 2
arr_sum = sum(arr)
missing_number = total_sum - arr_sum

print(f"The missing number is: {missing_number}")
