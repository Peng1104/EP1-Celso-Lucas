# EP 2019-1: Pega os dados dos arquivos para o jogo

import json
from pathlib import Path

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
        data = []
        
        data.append("{")
        data.append("\t\"Inicio\": {")
        data.append("\t\t\"Titulo\": \"Saguão do perigo\",")
        data.append("\t\t\"Descrição\": \"Você está no saguão de entrada do Insper\",")
        data.append("\t\t\"Opções\": {")
        data.append("\t\t\t\"Andar do Professor\": \"Pegar o elevador para ir ao andar do professor\",")
        data.append("\t\t\t\"Biblioteca\": \"Ir para a biblioteca\"")
        data.append("\t\t}")
        data.append("\t}, \"Andar do Professor\": {")
        data.append("\t\t\"Titulo\": \"Andar do desespero\",")
        data.append("\t\t\"Descrição\": \"Você chegou no andar da sala do seu professor\",")
        data.append("\t\t\"Opções\": {")
        data.append("\t\t\t\"Inicio\": \"Tomar o elevador para voltar ao saguão de entrada\",")
        data.append("\t\t\t\"Professor\": \"Ir falar com o professor\"")
        data.append("\t\t}")
        data.append("\t}, \"Professor\": {")
        data.append("\t\t\"Titulo\": \"O monstro do Python\",")
        data.append("\t\t\"Descrição\": \"Você foi pedir para o professor adiar o EP. O professor revelou que é um monstro disfarçado e devorou sua alma.\",")
        data.append("\t\t\"Opções\": {}")
        data.append("\t}, \"Biblioteca\": {")
        data.append("\t\t\"Titulo\": \"Caverna da tranquilidade\",")
        data.append("\t\t\"Descrição\": \"Você está na biblioteca\",")
        data.append("\t\t\"Opções\": {")
        data.append("\t\t\t\"Inicio\": \"Voltar para o saguão de entrada\"")
        data.append("\t\t}")
        data.append("\t}")
        data.append("}")
        
        ListToFile("Cenarios.json", data)
        
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