# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lucas Hix, lucash@insper.edu.br
# - aluno B: Celso Diniz, celsohad@insper.edu.br

import Data

for string in Data.Introdução():
    print(string, end = "")
    
print()

cenarios = Data.Cenarios()

if len(cenarios) == 0:
    print("ERRO FATAL!! NÃO FOI POSSÍVEL CARREGAR OS CENARIOS!! Revise o arquivo Cenarios.json")

else:
    nome_cenario_atual = next(iter(cenarios))
    
    while True:
        if nome_cenario_atual not in cenarios:
            print("ERRO!! NÃO FOI POSSÍVEL CARREGAR O CENARIO: " + nome_cenario_atual + " ! Revise o arquivo Cenarios.json")
            break
        
        cenario_atual = cenarios[nome_cenario_atual]
        
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
            print("ERRO!! NÃO FOI POSSÍVEL CARREGAR AS OPÇÕES DO CENARIO: " + nome_cenario_atual + " ! Revise o arquivo Cenarios.json")
            break