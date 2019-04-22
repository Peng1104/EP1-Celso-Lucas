# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:29:34 2019

@author: lucas
"""

#Arquivo que guarda todas as variaveis originais do Jogo

#Texto de Introdução do Jogo
Introdução = [
    "Na hora do sufoco!",
    "------------------",
    "",
    "Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix...",
    "Amanhã eu começo o EP. Mas isso não deu certo...",
    "É o dia de entregar o EP e você está muuuuito atrasado!",
    "Você está na entrada do Insper, e quer procurar o professor para pedir um adiamento do EP (boa sorte...)"
 ]

#Chance de ser teleportado ao entrar em um cenario para outro cenraio aleatorio
Chance_de_Teleporte = 0.05

#Texto para quando o Jogador é teleportado
Texto_do_Teleporte = [
    "------------------------------------------------------------------------------",
    "                                  !!CUIDADO!!                                 ",
    "Onde estou??",
    "Eu bem que avisei você entrou num portal invisível e foi para em outro lugar!!",
    "------------------------------------------------------------------------------"
]

#Cenarios do Jogo
Cenarios = {
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
            "FabLab": "Ir para o FabLab"
        }
    },
    "FabLab": {
        "Titulo": "FabLab",
        "Descrição": "Você entrou no FabLab",
        "Opções": {
            "Terceiro Andar": "Voltar para o terceiro andar"
        }
    },
    "Sala da Vítoria": {
        "Titulo": "Sala da Vítoria",
        "Descrição": "Parabéns você foi teleportado para a Sala da Vítoria!!\nVocê conseguio o adiamento da EP!!\nGAME OVER!!",
        "Opções": {}
    }
}