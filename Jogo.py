# EP 2019-1: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Celso Diniz, celsohad@al.insper.edu.br
# - Henrique Feola, henriquegf1@al.insper.edu.br

import random
import Defaults
from YamlFile import YamlFile
#-------------------------
#import monstros
#import insper_monster 
#-------------------------

#Arquivo contendo todos as configurações do jogo
arquivo = YamlFile("Config.yml")

for string in arquivo.getStringList("Introdução", default_value=Defaults.Introdução):
    print(string)
    
print()

#Dicionario dos Cenarios
Cenarios = arquivo.getDic("Cenarios", default_value=Defaults.Cenarios)

if len(Cenarios) == 0:
    print("ERRO FATAL!! NÃO FOI POSSÍVEL CARREGAR OS CENARIOS!! Revise os Cenarios")

else:
    #Seleciona o primeiro cenario do dicionario
    nome_cenario_atual = next(iter(Cenarios))
    
    #FoiTeleportado garante a não repetição do teleporte (continuar jogo)
    FoiTeleportado = False
    
    while True:
        if nome_cenario_atual not in Cenarios:
            print("ERRO!! NÃO FOI POSSÍVEL CARREGAR O CENARIO: " + nome_cenario_atual + " ! Revise os Cenarios")
            break
        
        cenario_atual = Cenarios[nome_cenario_atual]
        
        #Teleporte Aleatorio
        
        if arquivo.getFloat("Teleporte.Chance", default_value=Defaults.Chance_de_Teleporte) >= random.random() and not FoiTeleportado:
            for string in arquivo.getStringList("Teleporte.Texto", default_value=Defaults.Texto_do_Teleporte):
                print(string)

            print()
            nome_cenario_atual = random.choice(tuple(Cenarios.keys()))
            FoiTeleportado = True
            continue
        
        FoiTeleportado = False
        
        #Jogo em si com verificações de existencia
        
        if "Titulo" in cenario_atual.keys():
            print(cenario_atual["Titulo"])
            
        if "Descrição" in cenario_atual.keys():
            print(cenario_atual["Descrição"])
            
        if "Opções" in cenario_atual.keys():
            opções = cenario_atual["Opções"]
            
            if len(opções) == 0:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                print("Você morreu!")
                break
            else:
                print("O que você fara a seguir?\n")
                
                for cenario, descrição_do_movimento in opções.items():
                    print(cenario + ": " + descrição_do_movimento)
                
                escolha = input("Sua escolha: ")
                
                while escolha not in opções:
                    print()
                    print("Faça uma esolha valida!\nSua opções são:\n")
                    
                    for cenario, descrição_do_movimento in opções.items():
                        print(cenario + ": " + descrição_do_movimento)
                    
                    escolha = input("Sua escolha: ")
                
                print()
                nome_cenario_atual = escolha
        
        else:
            print("ERRO!! NÃO FOI POSSÍVEL CARREGAR AS OPÇÕES DO CENARIO: " + nome_cenario_atual + " ! Revise os Cenarios")
            break

#Salva o arquivo
arquivo.save()