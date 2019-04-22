# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:48:39 2019

@author: User
"""
## DESAFIO EXTRA1: Combate ate um morrer
## DESAFIO EXTRA2: O vilâo/jogador pode fuigir da batalha??
import random
### Combate 


Vida1 = float(input("insira o nivel de Vida do P1: "))
VidaJ = float(input("insira o nivel de Vida do PJ: "))

while Vida1 > 0 or VidaJ > 0:
    fugir = input("QUER FUGIR SEU MEDROSO?").lower()
        
    if random.randint(0, 20) and fugir == "sim":
        print("você escapou com sucesso!")
        break
    else:
            
        Poder1 = float(input("insira o nivel de Poder do P1: "))
        PoderJ = float(input("insira o nivel de Poder do PJ: "))
        
        Vida1 = Vida1 - PoderJ
        VidaJ = VidaJ - Poder1
            
        Feiura1 = float(input("insira o nivel de Feiura do P1: "))
        FeiuraJ = float(input("insira o nivel de Feiura do PJ: "))
    
        print("jogador com {0} de vida e monstro com {1}".format(VidaJ, Vida1))
    
       
            
if VidaJ > Vida1:
    print("Parabens! Você conseguiu sobreviver para tentar terminar o EP1!")
else:
    print("Você perdeu para um vilão ridiculo meramente ficcional... Mas perder você perdeu")

print("você ficou com {0} de vida".format(VidaJ))       