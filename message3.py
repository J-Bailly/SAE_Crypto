msg = "AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG F VGVXVGGD VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG"

def tri_du_message(str, cle):
    table = []
    for i in range(len(cle)):
        table.append([])
        for j in range(len(str)//len(cle)):
            table[i].append(str[i*len(cle)+j])
    
    cle2 = sorted(cle)
    table_trie = []
    for lettre in cle :
        table_trie.append(table[cle2.index(lettre)])
    return table_trie

def message_reforme(table):
    message = ""
    for i in range(len(table[0])):
        for j in range(len(table)):
            message += table[j][i]
    return message
print(tri_du_message(msg, "CRYPTO"))
print(message_reforme(tri_du_message(msg, "CRYPTO")))

def decryptage(message, cle, chaine_matrice, cle_ADFGVX):
    table = tri_du_message(message, cle)
    message = message_reforme(table)
    message_decrypte = ""
    message_trie = ""
    for i in range(len(table[0])):
        for j in range(len(table)):
            message_trie += table[j][i]