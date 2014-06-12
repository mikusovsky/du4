def pow(i):
    return i*i

def mpow(i,k):
    res = 1;
    for j in range(k):
        res *= i
    return res

exit = 1
while exit:
    fu = input('Please enter a function:')
    in1 = 1
    in2 = 1
    if fu == "pow":
        in1 = input('get value:')
        print(pow(int(in1)))
    elif fu == "mpow":
        in1 = input('get value i:')
        in2 = input('get value k:')
        print(mpow(int(in1),int(in2)))
    else:
        exit = 0
    