"""
Programme qui peut verifier si une chaine de caractere est un palindrome
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    Fonction secondaire "ispalindrome" qui verifie si la chaine de caractere est bien un palyndrome

    args: chaine de char

    return: true or false

    """

    # votre code ici
    p = p.lower()
    x = p.maketrans( "àâäéèêëîïôöùûüÿç" , "aaaeeeeiioouuuyc"," ?! :/',[].-_")
    p = p.translate(x)

    if p == p[::-1]:
        return True

    return False

#### Fonction principale

def main():
    """
    Appele de fonction secondaire verifier si des chaines de caracter sont des palindromes

    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
