from Logic.crud import add_cheltuiala, delete_cheltuiala
from Domain.cheltuiala import to_str
def new_menu():
    '''
    Meniu pentru consola noua
    :return:
    '''
    print('''
    Tasteaza comenzile separate prin ";". Comenzi acceptate: add, delete, showall, exit, help.
    Tasteaza "help" pentru a afla detalii despre comenzi.
    ''')

def help():
    '''
    Functie prin intermediul careia se definesc comenzile:
    add,
    :return:
    '''
    print('''
    help: arata meniu
    add, <id>,<nr_ap>,<suma>,<data>,<tipul>: adauga cheltuiala
    delete,<id>: sterge cheltuiala
    showall: arata toate cheltuielile
    exit: inchidere program
    ''')

def show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(to_str(cheltuiala))

def run_comenzi(cheltuieli):
    while True:
        print(new_menu())
        exit = False
        comanda = input("Tastati comenzile despartite de ';': ").split(';')
        for i in range(len(comanda)):
            action = comanda[i].split(',')
            if action[0] == 'help':
                help()
            elif action[0] == 'add':
                try:
                    cheltuieli = add_cheltuiala(cheltuieli, action[1], action[2], action[3], action[4], action[5], [], [])
                except IndexError as ie:
                    print(f"Eroare: {ie}")
            elif action[0] == 'delete':
                cheltuieli = delete_cheltuiala(cheltuieli, action[1], [], [])
            elif action[0] == 'showall':
                show_all(cheltuieli)
            elif action[0] == 'exit':
                exit = True
                break
        if exit is True:
            print("Programul s-a oprit")
            break