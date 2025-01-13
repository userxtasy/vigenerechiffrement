
                                              __                                      
                                             /\ \__                                   
                                        __  _\ \ ,_\    __      ____  __  __    ____  
                                       /\ \/'\\ \ \/  /'__`\   /',__\/\ \/\ \  /',__\ 
                                       \/>  </ \ \ \_/\ \L\.\_/\__, `\ \ \_\ \/\__, `\
                                        /\_/\_\ \ \__\ \__/.\_\/\____/\/`____ \/\____/
                                        \//\/_/  \/__/\/__/\/_/\/___/  `/___/> \/___/ 
                                                                          /\___/      
                                                                          \/__/       

                                                      -..- - .- ... -.-- ...
                                                  ..    .- --    .-    --. --- -..                                     
                                  ..    -. . . -..    - ---    -... .    -.. . ... - .-. --- -.-- . -..


# Qu'est ce que le chiffrement ?

C'est une méthode qui sert à transformer un message/texte compréhensible en un message/texte incompréhensible pour une personne ne connaissant pas la méthode de chiffrement dans le cas d'un chiffre monoalphabétique (cipher de César) ou dans le cas d'un chiffre polyalphabétique, pour une personne ne connaissant la clé de déchiffrement. 

# Vigenere Cipher ( chiffre de Vigenère )

Le cipher de Vigenère est une méthode chiffrement à clé. Sans clé le code ne peut être déchiffré. On utilise pour déchiffré majoritairement le tableau ci dessous :



### Voici comment cela fonctionne :

On commence avec un message clair, par exemple : "BONJOUR".
On choisit un mot clé, par exemple : "CLEF".
On répète le mot clé autant de fois que nécessaire pour couvrir tout le message : CLEFCLE.
Chaque lettre du message est alors décalée différemment en fonction de la lettre correspondante du mot clé. Par exemple :
La première lettre "B" est décalée selon "C" (décalage de 2).
La deuxième lettre "O" est décalée selon "L" (décalage de 11).
Et ainsi de suite.

_Résultat :_
_Message clair : BONJOUR_
_Mot clé répété : CLEFCLE_
_Message chiffré : DQRNFYU_

