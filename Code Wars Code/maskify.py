# def maskify(cc):
#     dd= ''
#     if len(cc) > 4:
#         last_four_char = cc[len(cc) - 4:len(cc)]
#         for i in range(len(cc) - 4):
#             dd += "#"
#         dd += last_four_char
    
#     else:
#         return cc

#     return dd

def maskify(cc):
    if len(cc) > 4:
        return "#" * (len(cc) - 4) + cc[-4:]
    else:
        return cc

cc = "13145141231351"
thicc = maskify(cc)
print(thicc)