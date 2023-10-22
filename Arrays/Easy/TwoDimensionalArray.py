n = int(input())
arr = []
for i in range(n):
    values = input().split()
    row = [int(val) for val in values]
    arr.append(row)

for i in range(n):
    arr[i][0], arr[i][1] = arr[i][1], arr[i][0]

# Print the swapped values
for row in arr:
    print(*row)

#by using the asterisk (*) before row as print(*row), we are unpacking the elements of the row list. 
# This means that each element of the list is treated as a separate argument to print(), 
# resulting in the elements being printed with a space between them
