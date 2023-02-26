def linearni_rce(a,b):
    if a == 0:
        if b == 0:
            return "Celé R"
        else:
            return "Nemá řešení"
    else:
        return -b/a