def binary_array_to_number(arr):
    # your code
    for num in arr:
        if num == 1:
            print(arr.index(num))


arr = [1,0,1,0] # Equals to 10
print(binary_array_to_number(arr))