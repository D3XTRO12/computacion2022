main_word = str(input("Ingrese una palabra o frase:"))
def no_string(main_word):
    if main_word[0:2] == 'no':
        print(main_word)
    else:
        print('no '+ main_word)

no_string(main_word)
