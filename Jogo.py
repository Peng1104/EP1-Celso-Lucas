# EP 2019-1: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Celso Diniz, celsohad@al.insper.edu.br
# - Henrique Feola, henriquegf1@al.insper.edu.br

import random
import Defaults
from YamlFile import YamlFile

#Arquivo contendo todos as configurações do jogo
arquivo = YamlFile("Config.yml")

for string in arquivo.getStringList("Introdução", default_value=Defaults.Introdução):
    print(string)
    
print()

#Dicionario dos Cenarios
Cenarios = arquivo.getDict("Cenarios", default_value=Defaults.Cenarios)

if len(Cenarios) == 0:
    print("ERRO FATAL!! NÃO FOI POSSÍVEL CARREGAR OS CENARIOS!! Revise os Cenarios")

else:
    #Seleciona o primeiro cenario do dicionario
    nome_cenario_atual = next(iter(Cenarios))
    
    #FoiTeleportado garante a não repetição do teleporte (continuar jogo)
    FoiTeleportado = False
    
    #Vida do Jogador
    Vida_Jogador = arquivo.getFloat("Combate.Vida do Jogador", default_value=Defaults.Vida_Inicial)

    #Dano Base do Jogador
    Dano_Base_Jogador = arquivo.getFloat("Comabte.Dano do Jogador", default_value=Defaults.Dano_Padrão_Jogador)

    #Contador de Combates
    Contador_de_Combates = 0

    while True:
        if nome_cenario_atual not in Cenarios:
            print("ERRO!! NÃO FOI POSSÍVEL CARREGAR O CENARIO: " + nome_cenario_atual + " ! Revise os Cenarios")
            break
        
        cenario_atual = Cenarios[nome_cenario_atual]
        
        #Teleporte
        
        #Chance de Teleporte
        if arquivo.getFloat("Teleporte.Chance", default_value=Defaults.Chance_de_Teleporte) >= random.random() and not FoiTeleportado:
            #Texto do Teleporte
            for string in arquivo.getStringList("Teleporte.Texto", default_value=Defaults.Texto_do_Teleporte):
                print(string)

            print()
            #Lugar aleatorio para ser teleportado
            nome_cenario_atual = random.choice(tuple(Cenarios.keys()))
            FoiTeleportado = True
            continue
        
        FoiTeleportado = False
        
        #Combate

        #Chance de Combate
        if arquivo.getFloat("Combate.Chance", default_value=Defaults.Chance_de_Combate) >= random.random():
            Monstros = arquivo.getDict("Combate.Monstros", default_value=Defaults.Monstros)

            #Pega um monstro aleatorio para o comabate
            Monstro = Monstros[random.choice(tuple(Monstros.keys()))]
            
            #Printa o Nome Real do Monstro
            if "Nome" in Monstro.keys():
                print(Monstro["Nome"])
            
            print()
            
            #Printa a Descrição do Monstro (o que aconeteceu para encontar o mesmo)
            if "Descrição" in Monstro.keys() and type(Monstro["Descrição"]) == list:
                for string in Monstro["Descrição"]:
                    print(string)
            
            print()
            
            #Pega as Opções para o combate
            if "Opções" in Monstro.keys() and type(Monstro["Opções"]) == dict:
                #Printa as opções
                for opção, descrição in Monstro["Opções"].items():
                    print(opção + ": " + descrição)

                print()

                opção = input("Que opção você vai seguir?\nSua escolha: ").lower()

                #Iniciar o Combate
                if random.random() > arquivo.getFloat("Combate.Chance de Fulga", default_value=Defaults.Chace_de_Fuga) or opção == "socar ele":
                    if "Vida" in Monstro.keys() and "Ataque Padrão" in Monstro.keys():
                        Vida_Monstro = float(Monstro["Vida"])
                        Dano_Padrão_Monstro = float(Monstro["Ataque Padrão"])

                        print("Hora do Duelo!!")
                        print()
                        print("Sua Vida: {0}".format(Vida_Jogador))
                        print("Vida do Mosntro: {0}".format(Vida_Monstro))
                        print()

                        while Vida_Jogador > 0 and Vida_Monstro > 0:
                            fugir = input("Quer fugir seu medroso?\nFugir?: ").lower()

                            if random.random() <= arquivo.getFloat("Combate.Chance de Fulga") and fugir == "sim":
                                print("Você escapou com sucesso!")
                                break
                            else:
                                Dano_Jogador = 0

                                if random.random() <= arquivo.getFloat("Comabte.Sorte do Monstro", default_value=Defaults.Sorte_Monstro):
                                    Dano_Jogador = Dano_Padrão_Monstro*2
                                else:
                                    Dano_Jogador = Dano_Padrão_Monstro

                                Dano_Monstro = 0

                                if random.random() <= arquivo.getFloat("Combate.Sorte do Jogador", default_value=Defaults.Sorte_Jogador):
                                    Dano_Monstro = Dano_Base_Jogador*2
                                else:
                                    Dano_Monstro = Dano_Base_Jogador

                                Vida_Jogador = Vida_Jogador - Dano_Jogador
                                Vida_Monstro = Vida_Monstro - Dano_Monstro

                                print()
                                print("Você levou {0} de Dano e deu {1} de Dano no Monstro".format(Dano_Jogador, Dano_Monstro))
                                print("Você está com {0} de Vida e o Monstro está com {1} de Vida".format(Vida_Jogador, Vida_Monstro))
                                print()

                        if Vida_Jogador > 0:
                            print("Parabens! Você conseguiu sobreviver para tentar terminar o EP1!")

                            Contador_de_Combates = Contador_de_Combates + 1
                            Recuperação = arquivo.getFloat("Comabte.Recuperação de Vida", default_value=Defaults.Recuperação)*Contador_de_Combates
                            Vida_Jogador = Vida_Jogador + Recuperação

                            print("Como você derotou o Monstro ganhou {0} de Vida! Ficando com {1} de Vida".format(Recuperação, Vida_Jogador))
                            print()
                        else:
                            print("Você perdeu para um vilão ridiculo meramente ficcional... Mas perder você perdeu")
                            break
        
        #Mudança de cenario
        
        #Printa o Tituto do cenario atual
        if "Titulo" in cenario_atual.keys():
            print(cenario_atual["Titulo"])
        
        #Printa a Descrição do cenario atual
        if "Descrição" in cenario_atual.keys() and type(cenario_atual["Descrição"]) == list:
            for string in cenario_atual["Descrição"]:
                print(string)
        
        #Entra nas opções do cenario
        if "Opções" in cenario_atual.keys() and type(cenario_atual["Opções"]) == dict:
            opções = cenario_atual["Opções"]
            
            #Venceu ou Perdeu o Jogo
            if len(opções) == 0:
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
