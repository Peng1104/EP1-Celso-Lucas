M = {


    'Inicio': { 'Seguranca' : 10 , 'Sem carteirinha' : 10 , 'Professor' : 100 , 'Limpeza' : 100 , 'Novo aluno' : '100' },
    'Andar do Professor': { 'Professor' : 100 , 'Sem computador' : 100 , 'Nao fez o EP' : 100 , 'M4' : 'P4' , 'M5' : 'P5' },
    'Professor': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'Biblioteca': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'Predio Novo': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'Primeiro Andar': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'Segundo Andar': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'Terceiro Andar': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
    'Fab Lap': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
}


print('Escolha um cenario e um monstro: ')

cenario = input('Sala: ')
monstro = input('Monstro: ')

print(insper_monster[cenario][monstro])


#-------------------------------------------- Funcao


def insper_monster(a,b):

	M = {

	#'nome da sala': { 'monstro 1' : 'poder monstro 1' , 'monstro 2' : 'poder monstro 2' , 'monstro 3' : 'poder monstro 3' , 'monstro 4' : 'poder monstro 4' , 'monstro 5' : 'poder monstro 5' },

	    'S1': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
	    'S2': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
	    'S3': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
	    'S3': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
	    'S4': { 'M1' : 'P1' , 'M2' : 'P2' , 'M3' : 'P3' , 'M4' : 'P4' , 'M5' : 'P5' },
	}


#	sala = input('Cenario: ')
#	monstro = input('Monstro: ')

	#return M[cenario][monstro]
	return M[a][b]

	
cenario = input('Cenario: ')
monstro = input('Monstro: ')

print(insper_monster(cenario, monstro))
