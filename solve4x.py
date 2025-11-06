operator = 0
equals = 0
def add(a, b, c):
    x = (c - b)/a
    return x
def subtract(a,b,c):
    x =(c + b)/a
    return x
def mult(a,b,c):
    x =(c//b)/a
    return x
def divide(a,b,c):
    x =(c*b)/a
    return x
while 1>0:
    w = input("what problem do you want to solve")
    for x in range(len(w)):
        if "+"==w[x]:
            operator = x
        if "-"==w[x]:
            operator = x
        if "*"==w[x]:
            operator = x
        if "D"==w[x]:
            operator = x
        if "="==w[x]:
            z = x+1
            equals = x


    if w[operator]=="+":
        print(add(int(w[:operator-1]),(int(w[operator+1:equals])),(int(w[1+equals:]))))
    if w[operator]=="-":
        print(subtract(int(w[:operator-1]),(int(w[operator+1:equals])),(int(w[1+equals:]))))
    if w[operator]=="*":
        print(mult(int(w[:operator-1]),(int(w[operator+1:equals])),(int(w[1+equals:]))))
    if w[operator]=="D":
        print(divide(int(w[:operator-1]),(int(w[operator+1:equals])),(int(w[1+equals:]))))