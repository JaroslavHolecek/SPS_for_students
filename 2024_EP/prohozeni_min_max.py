x = 5 # = znamená ulož
y = 8
print("Původní hodnota x a y:", x, y)

# Prohození hodnot x a y
z = x
x = y
y = z
print("Prohozená hodnota x a y:", x, y)

x, y = y, x
print("Prohozená hodnota x a y (druhá metoda):", x, y)

