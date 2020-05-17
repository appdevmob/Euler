#print(sum([x for x in range(1000) if (x%5==0) or (x%3==0)]))

def inVar(m1, m2, cap, itdivs = []):
    for x in range(cap):
        if (x%m1==0 or x%m2==0):
            itdivs.append(x)
    return itdivs

def getInputs():
    x = int(input("please enter m1? "))
    y = int(input("please enter m2? "))
    z = int(input("please enter cap? "))
    return x, y, z
            
a, b, c = getInputs()
print(sum(inVar(a, b, c)))


