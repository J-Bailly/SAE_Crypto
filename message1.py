lettreString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def dechiffrage1(code, message):
    messages_decode = ""
    for lettre in message:
        if lettre.isalpha():
            lettre_code = (lettreString.index(lettre) - code)%26 
            messages_decode += lettreString[lettre_code]
        else:
            messages_decode += lettre
    return messages_decode
            
        
print(dechiffrage1(12, "OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X' \nUZPUHGXSMNXQ EQODQF PQ OQFFQ \nZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ \nCGU FDAGHQDM XM OXQ?"))
