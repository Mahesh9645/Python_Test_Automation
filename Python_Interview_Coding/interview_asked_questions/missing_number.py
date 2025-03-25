arr = [0, 1, 2, 4, 5, 6, 7]  # 3 is missing
n = len(arr)  # Since the numbers are from 0 to n
total_sum = (n * (n + 1)) // 2 #28
arr_sum = sum(arr) #25
missing_number = total_sum - arr_sum

print(f"The missing number is: {missing_number}")

# Output: The missing number is: 3

################################################


word = "people tech group is a good company"

word1 = word.split()  # Splitting the sentence into words
output = ""  # Initialize an empty string

# Looping through the list in reverse order
for i in range(len(word1) - 1, -1, -1):
    output += word1[i] + " "

print(output.strip())  # Using strip() to remove the extra space at the end


# Output:company good a is group tech people

################################################
word = "RRSSTUV"

non_duplicate = " "

for i in word:
    if i not in non_duplicate:
        non_duplicate = non_duplicate + i
        
print(non_duplicate)

# Output: RSTUV
################################################