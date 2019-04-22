from monstros import *

print(Monstros.keys())
monstro = input('teste, escolha um monstro: ')
print(Monstros[monstro]['Nome'])

descricao = input('deseja descricao do monstro(sim/nao)? ')
if descricao == str('sim'):
    print(Monstros[monstro]['Descrição'])
if descricao == str('nao'):
    print('ok')
opcoes = input('Opcoes de ataque(s/n)? ')
if opcoes == str('sim'):
    print(Monstros[monstro]['Opções'].keys())    
else:
    print('ok')
opcoes_detalhes = input('descricao detalhada das opcoes(s/n)?')
if opcoes_detalhes == str('sim'):
    print(Monstros[monstro]['Opções'].values())
else:
    print('ok')
