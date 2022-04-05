# def gimme(input_array):
#     sorted_list = sorted(input_array)
#     mid_num = sorted_list[1]
#     return input_array.index(mid_num)
    
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])
    
x = gimme([5,10,14])
print(x)