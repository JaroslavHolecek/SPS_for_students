def euklid(X,Y):
    while X > 0 and Y > 0:
        if X < Y:
            Y = Y - X
        else:
            X = X - Y

    if X == 0:
        return Y
    else:
        return X

a = 15
b = 4
print(f"Nejvetsi spolecny delitel {a} a {b} je {euklid(a,b)}")

