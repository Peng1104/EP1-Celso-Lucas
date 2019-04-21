# EP 2019-1: Pega os dados dos arquivos para o jogo

import json
import re
from pathlib import Path
#----------------------------- funcao e arquivo (A decidir)
#import monstros
#import insper_monster
#-----------------------------



teleportchance = -1

def FileExists(filepath):
    if type(filepath) != str:
        return False
    
    return Path(filepath).is_file()

def ListToFile(filepath, data):
    if type(filepath) != str or type(data) != list:
        return False
    if FileExists(filepath):
        return False
    with open(filepath, 'w') as file:
        for item in data:
            file.write("{0}\n".format(item))
    return True

def Cenarios():
    if FileExists("Cenarios.json"):
        with open("Cenarios.json",'r') as file:
            return json.loads(file.read())
    else:
        cenarios = {
                "Inicio": {
                        "Titulo": "Saguão do perigo",
                        "Descrição": "Você está no saguão de entrada do Insper",
                        "Opções": {
                                "Andar do Professor": "Pegar o elevador para ir ao andar do professor",
                                "Biblioteca": "Ir para a biblioteca",
                                "Predio Novo": "Ir para a entrada do prédio novo"
                        }
                },
                "Andar do Professor": {
                        "Titulo": "Andar do desespero",
                        "Descrição": "Você chegou no andar da sala do seu professor",
                        "Opções": {
                                "Inicio": "Tomar o elevador para voltar ao saguão de entrada",
                                "Professor": "Ir falar com o professor"
                        }
                },
                "Professor": {
                        "Titulo": "O monstro do Python",
                        "Descrição": "Você foi pedir para o professor adiar o EP. O professor revelou que é um monstro disfarçado e devorou sua alma.",
                        "Opções": {}
                },
                "Biblioteca": {
                        "Titulo": "Caverna da tranquilidade",
                        "Descrição": "Você está na biblioteca",
                        "Opções": {
                                "Inicio": "Voltar para o saguão de entrada"
                        }
                },
                "Predio Novo": {
                        "Titulo": "Prédio Novo",
                        "Descrição": "Você crusou a rua e entrou no prédio novo",
                        "Opções": {
                                "Inicio": "Voltar para o saguão de entrada do Insper",
                                "Primeiro Andar": "Subir de escada para o primeiro andar",
                                "Segundo Andar": "Pegar o elevador para o segundo andar",
                                "Terceiro Andar": "Pegar o elevador para o terceiro andar"
                        }
                },
                "Primeiro Andar": {
                        "Titulo": "Primeiro Andar",
                        "Descrição": "Você chegou no primeiro andar do prédio novo",
                        "Opções": {
                                "Predio Novo": "Voltar para a entrada do prédio novo decendo as escadas",
                                "Segundo Andar": "Subir de escada para o segundo andar",
                                "Terceiro Andar": "Pegar o elevador para o terceiro andar"
                        }
                },
                "Segundo Andar": {
                        "Titulo": "Segundo Andar",
                        "Descrição": "Você chegou no segundo andar do prédio novo",
                        "Opções": {
                                "Predio Novo": "Voltar para a entrada do prédio novo atravez do escorregador",
                                "Primeiro Andar": "Descer de escada para o primeiro andar",
                                "Terceiro Andar": "Subir de escada para o terceiro andar"
                        }
                },
                "Terceiro Andar": {
                        "Titulo": "Terceiro Andar",
                        "Descrição": "Você chegou no terceiro andar do prédio novo",
                        "Opções": {
                                "Predio Novo": "Voltar para a entrada do prédio novo decendo de elevador",
                                "Primeiro Andar": "Pegar o elevador para o primeiro andar",
                                "Segundo Andar": "Descer de escada para o segundo andar",
                                "Fab Lap": "Ir para o Fab Lap"
                        }
                },
                "Fab Lap": {
                        "Titulo": "Fab Lap",
                        "Descrição": "Você entrou no Fab Lap",
                        "Opções": {
                            "Terceiro Andar": "Voltar para o terceiro andar"
                        }
                }
        }
        with open("Cenarios.json", 'w') as file:
            file.write(json.dumps(cenarios, ensure_ascii=False, indent="\t"))
        
        return Cenarios()

def Introdução():
    if FileExists("Introdução.txt"):
        with open("Introdução.txt",'r') as file:
            return file.readlines()
    else:
        data = []
        
        data.append("Na hora do sufoco!")
        data.append("------------------")
        data.append("")
        data.append("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix...")
        data.append("Amanhã eu começo o EP. Mas isso não deu certo...")
        data.append("É o dia de entregar o EP e você está muuuuito atrasado!")
        data.append("Você está na entrada do Insper, e quer procurar o professor para pedir um adiamento do EP (boa sorte...)")
        
        ListToFile("Introdução.txt", data)
        
        return Introdução()

def getTeleportText():
    if FileExists("Teleporte.txt"):
        with open("Teleporte.txt",'r') as file:
            return file.readlines()
    else:
        data = []
        
        data.append("------------------")
        data.append("Ops... você acabou de entrar num portal...")
        data.append("Onde estou??")
        data.append("------------------")
        
        ListToFile("Teleporte.txt", data)
        
        return getTeleportText()

def getTeleportChance():
    global teleportchance
    if teleportchance != -1:
        return teleportchance
    elif FileExists("Config.txt"):
        with open("Config.txt",'r') as file:
            data = file.readlines()
            
        for i in range(len(data)):
            if data[i].startswith("Chance de Teleporte: "):
                if re.search("^1|0(.\d{1,2})?$", data[i].split()[3]):
                    teleportchance = float(data[i].split()[3])
                    return getTeleportChance()
                else:
                    data[i] = "Chance de Teleporte: 0.05"
                    with open("Config.txt", 'w') as file:
                        for e in data:
                            file.write(e + "\n")
                    teleportchance = 0.05
                    return getTeleportChance()
    else:
        with open("Config.txt", 'a') as file:
            file.write("Chance de Teleporte: 0.05")
            teleportchance = 0.05
            return getTeleportChance()
