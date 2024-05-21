inventario = {'espada': 1, 'machado': 2, 'picareta': 1, 'pão': 4, 'remédio': 6}

contador = 100

while 1 < contador:
    print('INVENTÁRIO:')
    print(' 1. Adicionar itens \n 2. Remover itens \n 3. Mostrar inventário \n 4. Sair')
    opcao = int(input('Escolha a opção desejada: '))
    print(' ')

    if opcao == 1:
        item = input('Adicionar item: ')
        inventario[item] = input('Adicionar quantidade: ')
        print(inventario)
        continuar = input('Deseja continuar a adicionar? ')
        if continuar == 'sim':
            while continuar == 'sim':
                item = input('Adicionar item: ')
                inventario[item] = input('Adicionar quantidade: ')
                print(inventario)
                continuar = input('Deseja continuar a adicionar? ')
                if continuar != 'sim':
                    break
        print(' ')

    elif opcao == 2:
        print('Alterar qauntida ou apagar item')
        item = input('Esolher item: ')
        print(' ')
        if item in inventario:
            inventario[item] = int(input('Alterar quantidade: '))
            if inventario[item] == 0:
                del inventario[item]
            print(inventario)
            continuar = input('Deseja continuar a adicionar? ')
            print(' ')
        else:
            print('Item não enconmtrado')
            continuar = input('Deseja continuar a adicionar? ')
            print(' ')
            
         
        if continuar == 'sim':     
            while continuar == 'sim':
                print('Alterar qauntida ou apagar item')
                item = input('Esolher item: ')
                print(' ')
                if item in inventario:
                    inventario[item] = int(input('Alterar quantidade: '))
                    if inventario[item] == 0:
                        del inventario[item]
                    print(inventario)
                    continuar = input('Deseja continuar a adicionar? ')
                    print(' ')
                else:
                    print('Item não enconmtrado')
                    continuar = input('Deseja continuar a adicionar? ')
                    print(' ')
                if continuar != 'sim':
                    break           
            print(' ')      

    elif opcao == 3:
        print(f'O seu inventario ', inventario)
        print(' ')

    elif opcao == 4:
        print ('Saindo...')
        print(' ')
        break