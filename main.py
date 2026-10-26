tarefas=[]
r='1'
resp1='S'

while True:
    
    r=int(input('___________________\n'+
          '1.Adicionar Tarefas.\n'+
          '2.Listar Tarefas.\n'+
          '3.Remover Tarefas.\n'+
          '4.Sair do Programa.\n'+
          '_____________________\n'+
          'O que deseja fazer?: \n'))
    
    if r==1:
        
        resp1='S'
        while resp1=='S':
            tarefas.append(input('Qual tarefa deseja incluir?: '))
            resp1 = str(input('Deseja adicionar mais uma tarefa? S/N:')).upper()
    
    elif r==2:
        
        print('Estas são suas tarefas:')
        for i, tarefa in enumerate(tarefas, start=1):
            print(i,tarefa)
    
    elif r==3:
        if len(tarefas)>0:
            print('Estas são sua Tarefas:')
            for i, tarefa in enumerate (tarefas, start=1):
                print (i,tarefa)
                
            opção=int(input('Insira o numero do item que deseja excluir de sua lista:'))
            if 1<= opção <= len(tarefas):
                tarefas.pop(opção-1)
            else:
                print('Numero de tarefa invalido.')
        else:
            print('Sua lista está vazia.')
    
    elif r==4:
        break