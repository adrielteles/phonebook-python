import re
def valid_name(name: str):

    try:
        if len(name) >=3 and name.replace(' ','').isalpha():
            name = name.title()
            return name
        else:
            return False
    except ValueError as err:
        return err


def valid_phone(phone: str):

    try:
        if len(phone) == 12 and phone.isdecimal():
            phone = f"({phone[0:3]}) {phone[3:8]}-{phone[8:]}"
            return phone
        else:
            return False
    except ValueError as err:
        return err

def valid_mail(mail: str):

    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    try:
        if re.match(pat, mail):
            return mail
        else:
            return False
    except ValueError as err:
        return err


def valid_choice(choice_phrase:str):

    while True:
        choice = input(f"{choice_phrase} (Y/N)?")
        if choice == "y" or choice == "Y":
            return True
        elif choice == "n" or choice == "N":
            return False
        else:
            print("Opção invalida")
            continue