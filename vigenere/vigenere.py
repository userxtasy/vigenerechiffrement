#--------------------------------LOGO---------------------------------#

    #def couleur
RED = "\033[31m"
RESET = "\033[0m"
    #fin def couleur

print (RED + "                                           __  ")
print ("                                          /\ \__  ")                                  
print ("                                    __  _ \ \ ,_\    __      ____  __  __    ____ ")  
print ("                                   /\ \/'\ \ \ \/  /'__`\   /',__\/\ \/\ \  /',__\ ") 
print ("                                   \/>  </  \ \ \_/\ \L\.\_/\__, `\ \ \_\ \/\__, `\ ")
print ("                                    /\_/\_\  \ \__\ \__/.\_\/\____/\/`____ \/\____/")
print ("                                    \//\/_/   \/__/\/__/\/_/\/___/  `/___/> \/___/") 
print ("                                                                      /\___/")      
print ("                                                                      \/__/")       
print ("                                                                      ")
print ("                                                  -..- - .- ... -.-- ...")
print ("                                              ..    .- --    .-    --. --- -..")                     
print ("                              ..    -. . . -..    - ---    -... .    -.. . ... - .-. --- -.-- . -.." + RESET)
#-----------------------------fin logo----------------------------------#

def chiffrement (func_texte, func_code):
    print (f"en cour de chiffrement de : '{func_texte}'")
    return_texte = []
    func_texte = func_texte.upper() #majuscule
    func_code = func_code.upper()   #majuscule
    len_func_code = len(func_code)  #taille code
    i = 0                           #index code 

    for character in func_texte:
        if character.isalpha():
            shift = ord(func_code[i]) - ord('A')
            nv_character = chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
            return_texte.append(nv_character)
            i = (i + 1) % len_func_code    
        else:
            return_texte.append(character)
    return ''.join(return_texte)

texte = input ("sentence to encrypt : ")
code = input ("code : ")
resultat = chiffrement(texte, code)
print (f"texte chiffré : {resultat}")
print (RED + "                                                      provided by xtasys" + RESET)
