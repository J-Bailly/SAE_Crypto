lettreString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def message2(cle:str, message:str) -> str:
    res = ""
    compteur = 0
    for lettreMessage in message:
        if lettreMessage in lettreString and lettreMessage.isalpha():
            lettreCle = cle[compteur]
            decrypt_letter = (lettreString.index(lettreMessage) - lettreString.index(lettreCle)) % 26
            res += lettreString[decrypt_letter]
            compteur = (compteur + 1) % len(cle)
        else:
            res += lettreMessage
    return res
        
print(message2("CINQ", "UCVLGH YUU BEQEMF TG ORETORI RIVDXQA \n QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O \n KEORBB"))

print(len("AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M"))