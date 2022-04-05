def create_phone_number(n):
    # first_three = ""
    # second_three = ""
    # last_four = ""

    # str_list = []
    # for i in range(len(n)):
    #     str_list.append(str(n[i]))
    
    # for num in str_list[:3]:
    #     first_three += num

    # for num in str_list[3:6]:
    #     second_three += num

    # for num in str_list[6:]:
    #     last_four += num

    # phone_number = "(" +first_three + ")" + " " + second_three + '-' + last_four

    # return phone_number

    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))
