from src.phoneBook import *

def main_menu(phoneBook: dict):
    while True:
        try:
            options_menu = ("1 Adicionar contato", "2 Procurar Contato", "3 Apagar contato", "4 Alterar contato", "5 Relatorio de contatos", "6 Sair")
            print(" ")
            print("--------------AGENDA-----------------")
            for option in options_menu:
                print(option)
            print(" ")
            print("--------------------------------------")
            print(" ")
            
            option = int(input('Selecionar Opção: '))
            if option in range(1, len(options_menu)+1):
                if option == 1:
                    create_contact(phoneBook)
                elif option == 2:
                    search_contact(phoneBook)
                elif option == 3:
                    delete_contact(phoneBook)
                elif option == 4:
                    update_contact(phoneBook)
                elif option == 5:
                    create_report(phoneBook)
                elif option == 6:
                    break
            else:
                print("Opção invalida")
                continue
        except ValueError:
            print("Opção invalida")
            continue
        except EOFError:
            break