#!/usr/bin/python3

# Usage: python3 cesar.py clef c/d phrase
# Returns the result without additional text


def cesar(cle , k , texte ):
    """
    @param cle : cle du chifrement ou déchifrement de cesar
    @param texte : le texte à chiffrer ou à déchiffrer (il doit etre en majuscule)
    @return result : le résultat du chiffrement ou déchiffrement
    """
    result = ""
    for c in texte:
        if k =="c":
            new_c = (ord(c)%ord('A') + ord(cle)%ord('A') )%26 + ord('A')
        elif k=="d":
            new_c = (ord(c)%ord('A') - ord(cle)%ord('A') )%26 + ord('A')
        result += chr(new_c)
    return result

print(cesar('R',"c","ATTAQUESURLUTECEDEMAIN"))
print(cesar('N',"d","IVIRYNPELCGBYBTVR"))