def pow(i):
    res = i*i
    return res

def mpow(i,k):
    res = 1;
    for j in range(k):
        res *= i
    return res

def empow(i,k):
        if k==0:
            return 1
        elif k==1:
            return x
        t = empow(i,k/2)
        t*=t;
        if k%2==1:
            t*=i
        return t

print(pow(2))
print(mpow(2,2))
print(empow(2,2))
print(pow(3))
print(mpow(3,2))
print(empow(3,2))


exit = 1
while exit:
    fu = input('Please enter a function:')
    if fu == "pow":
        in1 = input('get value:')
        print(pow(int(in1)))
    elif fu == "mpow":
        in1 = input('get value i:')
        in2 = input('get value k:')
        print(mpow(int(in1),int(in2)))
    elif fu == "empow":
        in1 = input('get value i:')
        in2 = input('get value k:')
        print(mpow(int(in1),int(in2)))
    else:
        exit = 0
    
