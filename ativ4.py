inventario = {'espada': 1, 'machado': 2, 'picareta': 1, 'pão': 4, 'remédio': 6}
print('INVENTÁRIO:')
print(' 1. Adicionar itens \n 2. Remover itens \n 3. Mostrar inventário \n 4. Sair')
opcao = int(input('Escolha a opção desejada: '))
print(' ')

def menu():
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
    inventario[item] = int(input('Alterar uantidade: '))
    if inventario[item] == 0:
        del inventario[item]
    print(inventario)
    continuar = input('Deseja continuar a adicionar? ')
    if continuar == 'sim':
        while continuar == 'sim':
            print('Alterar qauntida ou apagar item')
            item = input('Adicionar item: ')
            inventario[item] = int(input('Adicionar quantidade: '))
            if inventario[item] == 0:
                del inventario[item]
            print(inventario)
            continuar = input('Deseja continuar a adicionar? ')
            if continuar != 'sim':
                break           

    
    # item_deletar = input('Deletar item: ')
    # del inventario[item_deletar]
    # print(inventario)
    # continuar = input('Deseja continuar a deletar? ')    

    # if continuar == 'sim':
    #     while continuar == 'sim':
    #         item_deletar = input('Deletar item: ')
    #         del inventario[item_deletar]
    #         print(inventario)
    #         continuar = input('Deseja continuar a deletar? ')
    #         if continuar != 'sim':
    #             break
