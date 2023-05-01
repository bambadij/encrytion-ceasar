def chiffrement_cesar(texte, decalage):
    texte_chiffre = ""
    for caractere in texte:
        if caractere.isalpha():
            ascii_caractere = ord(caractere)
            ascii_caractere = (ascii_caractere - ord('a') + decalage) % 26 + ord('a')
            caractere_chiffre = chr(ascii_caractere)
        else:
            caractere_chiffre = caractere
        texte_chiffre += caractere_chiffre
    return texte_chiffre

# Exemple d'utilisation
texte_clair = input("Enter your message : ")
decalage = 3
texte_chiffre = chiffrement_cesar(texte_clair, decalage)
print("Texte clair: ", texte_clair)
print("Texte chiffré: ", texte_chiffre)