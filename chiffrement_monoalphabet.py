def monoalphabetic_chiffr(text_clair, cle): 
    chiffr_text = "" 
  
    for i in range(len(text_clair)): 
        if text_clair[i] in cle: #si la lettre du texte chiffré existe dans le disctionnaire de la clé
            chiffr_text += cle[text_clair[i]] 
        else: # Si le caractère n'est pas dans le dictionnaire, alors on l'ajoute tel quel au texte en clair.
            chiffr_text += text_clair[i] 
  
    return chiffr_text 
