from unicodedata import digit


def validate_pin(cadena):
    if cadena.isnumeric():
        if len(cadena) == 4 or len(cadena) == 6:
            return True
        else:
            return False
    else:
        return False