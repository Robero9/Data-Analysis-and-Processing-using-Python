vocale = 'aeiouAEIOU'
input_string = 'Salutare, ce mai faci?'

def functie_filtrare(ch):
    return ch not in vocale

print("".join(filter(functie_filtrare, input_string)))
