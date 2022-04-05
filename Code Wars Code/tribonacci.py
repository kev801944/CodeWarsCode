# def tribonacci(signature, n):
#     #your code here
#     trib_list = []
#     count = 0

#     if len(signature) < 3 or n == 0:
#         return []

#     n1 = signature[0]
#     n2 = signature[1]
#     n3 = signature[2]

#     while count < n:
#         trib_list.append(n1)
#         nth = n1 + n2 + n3
#         n1 = n2
#         n2 = n3
#         n3 = nth
#         count += 1
    
#     return trib_list

def tribonacci(signature, n):
    res = signature[:n]
    print(res)
    for i in range(n - 3):
        res.append(sum(res[-3:]))
        print(res[-3:])
    
    return res

def fibonacci(array):
    
    fib_list = []
    count = 0
    n1 = array[0]
    n2 = array[1]
    while count < len(array):
        fib_list.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

    return fib_list


# num = [0,1,2,3,4,5,6,7,8,9]
# print(fibonacci(num))
num = [1,1,1]
print(tribonacci(num,10))
