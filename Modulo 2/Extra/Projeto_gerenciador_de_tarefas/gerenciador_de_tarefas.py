import os

tarefas = {
    'tarefas' : ['Arrumar o quarto', 'Lavar a louça'],
    'datas' : [ '17/10', '17/10']
}


def mostrar_tarrefas():
    barra = f'|{35*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Data: {tarefas['datas'][i]}')
    input('| Aperte "ENTER" para continuar... ')

def adicionar_tarefas():
    barra = f'|{35*'-'}|'
    print(barra)
    tarefa = input('| Nome da nova tarefa: ')
    data = input('| Data: ')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('| Tarefa adicionada com sucesso!')
    input('| Aperte "ENTER" para continuar... ')

def remover_tarefas():
    barra = f'|{35*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
            print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Data: {tarefas['datas'][i]}')
    id_tarefa = int(input('| Digite o número da tarefa que deseja remover: '))
    
    if id_tarefa > 0:
        tarefa = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas['datas'].pop(id_tarefa-1)
    else:
        print('| ID inválido.')
    print(f'|Tarefa "{tarefa}" removida com sucesso! ')
    input('|Aperte "ENTER" para continuar...')

def menu():
    while True:
        try:
            os.system('cls')
            print('Remover tarefas')
            barra = f'|{35*'-'}|'
            print(barra)
            print('|    GERENCIADOR DE TAREFAS         |')
            print(barra)
            print('|        1- Mostrar tarefas         |')
            print('|        2- Adicionar tarefa        |')
            print('|        3- Remover tarefa          |')
            print('|        4- Sair                    |')
            print(barra)
            opc = int(input('| Escolha o número de opções: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarrefas()
            elif opc == 2:
                os.system('cls')
                adicionar_tarefas()
            elif opc == 3:
                os.system('cls')
                remover_tarefas()
            elif opc == 4:
                print('Saindo do programa...')
                break
            else:
                os.system('cls')
                print('Opção inválida!')
                input('Aperte "ENTER" para continuar...')
        except:
            print('ERRO! Escolha uma opção válida. ')
            input('Aperte "ENTER" para continuar...')
menu()