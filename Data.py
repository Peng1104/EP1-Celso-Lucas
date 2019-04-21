# EP 2019-1: Pega os dados do arquivo Config.yml

from YamlFile import YamlFile

File = YamlFile("Config.yml")

Introdução = []
Texto_do_Teleporte = []
Chance_de_Teleporte = -1
Cenarios = {}

def load():
    global File
    global Introdução
    global Texto_do_Teleporte
    global Chance_de_Teleporte
    global Cenarios
    
    Lista = []
        
    Lista.append("Na hora do sufoco!")
    Lista.append("------------------")
    Lista.append("")
    Lista.append("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix...")
    Lista.append("Amanhã eu começo o EP. Mas isso não deu certo...")
    Lista.append("É o dia de entregar o EP e você está muuuuito atrasado!")
    Lista.append("Você está na entrada do Insper, e quer procurar o professor para pedir um adiamento do EP (boa sorte...)")
        
    Introdução = File.getList("Introdução", default_value=Lista)
    
    Chance_de_Teleporte = File.getFloat("Teleporte.Chance", default_value=0.5)
    
    Lista = []
    
    Lista.append("------------------")
    Lista.append("Ops... você acabou de entrar num portal...")
    Lista.append("Onde estou??")
    Lista.append("------------------")
    
    Texto_do_Teleporte = File.getList("Teleporte.Texto", default_value=Lista)
    
    dic = {
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
            },
    }
    Cenarios = File.getDic("Cenarios", default_value=dic)
    
    File.save()