def linearni_rovnice(a, b):
    print(f'{a}x {b:+} == 0')
    if a == 0:
        if b ==0:
            return "Celé R"
        else:
            return "Nemá řešní"
    else:
        return -b/a

print(linearni_rovnice(2, 0))
print(linearni_rovnice(0, -5))
print(linearni_rovnice(9, -6))
print(linearni_rovnice(7, -6))
print(linearni_rovnice(0, 0))