a_sonrriendo = str(input("El mono a esta sonrriendo?: "))
b_sonrriendo = str(input("El mono b esta sonrriendo?: "))

def problemas_monos(a_sonrriendo, b_sonrriendo):
    z = False
    a_smile = False
    b_smile = False
    if a_sonrriendo == "si":
        a_smile = True
    if b_sonrriendo == "si":
        b_smile = True    
    if a_smile == True & b_smile == True:
        z = True
    elif a_smile == False & b_smile == False:
        z = True
    elif a_smile == False & b_smile == True:
        z = False

    return z

if problemas_monos(a_sonrriendo, b_sonrriendo) == True:
    print("We're in trouble")
elif problemas_monos(a_sonrriendo, b_sonrriendo) == False:
    print("We aren't in trouble")