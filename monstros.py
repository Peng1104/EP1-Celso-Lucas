#Esqueleto de dicionario com monstros ou viloes para as fases/salas do jogo (podendo haver mais monstros/ sala do que o jogo pois é um teste

M = {

#'nome da sala': { 'monstro 1' : 'poder monstro 1' , 'monstro 2' : 'poder monstro 2' , 'monstro 3' : 'poder monstro 3' , 'monstro 4' : 'poder monstro 4' , 'monstro 5' : 'poder monstro 5' },

    'S1': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'S2': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'S3': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'S3': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'S4': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
}

print('Escolha uma sala e um monstro: ')
sala = input('Sala: ')
monstro = input('Monstro: ')

print(M[sala][monstro])