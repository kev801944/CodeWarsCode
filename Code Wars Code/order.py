def order(sentence):
    # code here
    org_list = []
    sen_list = sentence.split()
    solution_list = []

    if sentence == '':
        return ''
    
    for char in sentence:
        if char.isdigit():
            org_list.append(char)
    org_list.sort()

    for ele in org_list:
        for word in sen_list:           
            if ele in word:
                solution_list.append(word)
                solution = " ".join(c for c in solution_list)

    return solution

sentence = "is2 Thi1s T4est 3a"
print(order(sentence))