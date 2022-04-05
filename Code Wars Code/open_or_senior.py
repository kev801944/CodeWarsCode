def open_or_senior(data):
    member_list = []
    for val in data:
        if val[0] >= 55 and val[1] > 7:
            member_list.append('Senior')
        else:
            member_list.append('Open')

    return member_list


# data = [(45, 12),(55,21),(19, -2),(104, 20)]
data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(data))