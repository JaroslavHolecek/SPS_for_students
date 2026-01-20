def linearni_rovnice(a, b):
    if a == 0:
        # v a je uložená nula7
        if b == 0:
            # v b je uložená nula
            return "Nekonečně mnoho řešení"
        else:
            # v b není uložená nula
            return "Nemá řešení"
    else:
        # v a není uložená nula
        return -b/a




