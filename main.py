def palidandrom(arg_lower):
    for text in arg_lower:
        pass

    for reversed_text in reversed(arg_lower):
        pass

    if(text == reversed_text):
        print("Podany text jest palindromem")
        return True
    else:
        print("Podany tekst nie jest palindromem")
        return False


arg = input("Wpisz słowo: ")
arg_lower = arg.lower()
palidandrom(arg_lower)

print(arg)
print(arg_lower)