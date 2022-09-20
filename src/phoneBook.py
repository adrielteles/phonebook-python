from src.validation import *
def init_phoneBook():
    phoneBook = {}
    return phoneBook

def create_contact(phoneBook: dict):

    try:
        while True:
            while True:
                name = valid_name(input('Nome: '))
                if name != False:
                    break
                elif name == False:
                    print("Nome invalido")
                    continue
                else:
                    print(name)
                    continue

            while True:
                phone = valid_phone(input('Phone: '))
                if phone != False:
                    break
                elif phone == False:
                    print("Telefone invalido")
                    continue
                else:
                    print(phone)
                    continue
            
            while True:
                mail = valid_mail(input('mail: '))
                if mail != False:
                    break
                elif mail == False:
                    print("e-mail invalido")
                    continue
                else:
                    print(mail)
                    continue
            
            phoneBook[name] = [phone, mail]
            addContact = search_contact(phoneBook, name)
            if addContact != False:
                print("Contato adicionado com sucesso")
                print(addContact)
            elif addContact == False:
                print("Contato não foi adicionado com sucesso (ERRO)")
            else:
                print(addContact)
                print("Erro ao adicionar contato")

            optionNewContact = False
            while True:
                newContact = input(str("Adicionar novo contato (Y/N)?"))
                if newContact == "y" or newContact == "Y":
                    optionNewContact = True
                    break
                elif newContact == "n" or newContact == "N":
                    optionNewContact = False
                    break
                else:
                    print("Opção invalida.")
                    continue
            if optionNewContact == True:
                continue
            elif optionNewContact == False:
                break
            else:
                ("Ocorreu um erro inesperado")
                    
    except ValueError as err:
        print(err)

def search_contact(phoneBook: dict, name=""):

    try:
        if len(name) > 1:
            name = valid_name(name)
            if name != False:
                if name in phoneBook.keys():
                    return f"{name}, {phoneBook[name][0]}, {phoneBook[name][1]}"

                elif name not in phoneBook.keys():
                    return False
                else:
                    return "Erro inesperado"
            elif name == False:
                return "Nome invalido"
            else:
                print(name)

        else:
            while True:
                name = valid_name(input("Procurar por nome: "))
                if name != False:
                    if name in phoneBook.keys():
                        print(f'{"Nome":<25}{"Telefone":<20}{"E-mail":<30}')
                        print(f"{name:<25}{phoneBook[name][0]:<20}{phoneBook[name][1]:<30}")
                        break

                    elif name not in phoneBook.keys():
                        print("Contato não encontrado")
                        continue
                    else:
                        print("Erro ao localizar contato")
                        break
                elif name == False:
                    print("Nome invalido")
                    continue
                else:
                    print(name)
                    break
  
    except ValueError as err:
        print(err)

def update_contact(phoneBook: dict):
    try:
        while True:
            while True:
                oldName = valid_name(input("Buscar por nome: "))
                if oldName != False:
                    break
                elif oldName == False:
                    print("Nome Invalido")
                    continue
                else:
                    print(oldName)
                    break
            contact = search_contact(phoneBook,name = oldName)
            if contact != False:
                print(contact)

                optionUpdate = valid_choice("Alterar contato")
                if optionUpdate == True:
                    while True:
                        newName = valid_name(input('Novo Nome: '))
                        if newName != False:
                            break
                        elif newName == False:
                            print("Nome invalido")
                            continue
                        else:
                            print(newName)
                            break

                    while True:
                        newPhone = valid_phone(input('Novo Telefone: '))
                        if newPhone != False:
                            break
                        elif newPhone == False:
                            print("Telefone invalido")
                            continue
                        else:
                            print(newPhone)
                            break
                            
                    while True:
                        newMail = valid_mail(input('Novo e-mail: '))
                        if newMail != False:
                            break
                        elif newMail == False:
                            print("e-mail invalido")
                            continue
                        else:
                            print(newMail)
                            break
                    phoneBook[newName] = phoneBook[oldName]
                    del phoneBook[oldName]
                    phoneBook[newName] = [newPhone, newMail]

                    contactUpdatedCall = search_contact(phoneBook, newName)
                    if contactUpdatedCall != False:
                        print("Contato Atualizado com sucesso")
                        print(contactUpdatedCall)
                        break
                    elif contactUpdatedCall == False:
                        print("Erro ao atualizar contato")
                        break
                    else:
                        print(contactUpdatedCall)
                        break

                elif optionUpdate == False:
                    break
                else:
                    print("Erro na operação")
                    break

            elif contact == False:
                print("Contato Não encontrado")
                continue
            else:
                print("Ocorreu um erro")
                break
            
    except ValueError as err:
        print(err)


def delete_contact(phoneBook:dict):
    
    while True:
        delContact = valid_name(input("Buscar por nome: "))
        if delContact !=False:
            contact = search_contact(phoneBook,name = delContact)
            if contact != False:
                print(contact)
            optionUpdate = valid_choice("Deletar Contato")
            if optionUpdate == True:
                del phoneBook[delContact]
                print("Contato deletado")
                break
            elif optionUpdate == False:
                break
            else:
                print("Erro na Operação")
                break
        elif delContact == False:
            print("Nome invalido")
            continue
        else:
            print(delContact)
            break


def create_report(phoneBook: dict):
    print(f'{"LISTA DE CONTATOS":^101}')
    print("-----------------------------------------------------------------------------------")
    print(f'{"Nro":<10}{"Nome":<25}{"Telefone":<20}{"E-mail":<30}')
    print("-----------------------------------------------------------------------------------")
    idContact = 1
    for name in phoneBook.keys():

        print(f'{idContact:<10}{name:<25}{phoneBook[name][0]:<20}{phoneBook[name][1]:<30}')
        idContact += 1
