from Domain.cheltuiala import *
from Logic.crud import add_cheltuiala, edit_cheltuiala, delete_cheltuiala
from Logic.operatiuni import add_value, sort_cheltuieli
from UserInterface.command_line_console import run_comenzi

def print_meniu():
    print('''
    MENIU
    1. CRUD 
    2. Operatiuni
    3. Undo/Redo
    n. Catre meniul nou
    x. Iesire
    ''')

def print_crud_meniu():
    print('''
    MENIU Crud
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate cheltuielile
    5. Inapoi
    ''')

def print_operatiuni_meniu():
    print('''
    MENIU Operatiuni
    1. Stergerea tuturor cheltuielilor unui apartament dat.
    2. Adunarea unei valori la toate cheltuielile dintr-o dată citită.
    3. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
    4. Ordonarea cheltuielilor descrescător după sumă.
    5. Afișarea sumelor lunare pentru fiecare apartament.
    6. Inapoi
    ''')

def run_crud_ui(cheltuieli):
    '''
    :param cheltuieli: lista de cheltuieli
    :return:
    '''

    def handle_show_all(cheltuieli):
        '''
        Afisare lista de cheltuieli din memorie
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        for cheltuiala in cheltuieli:
            print(to_str(cheltuiala))

    def handle_add_cheltuiala_ui(cheltuieli):
        '''
        Adaugam o cheltuiala citita de la tastatura in lista de cheltuieli
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id = input('Intorduceti ID-ul cheltuielii: ')
        nr_ap = input('Introduceti numarul apartamentului: ')
        suma = input('Introduceti suma: ')
        data = input('Introduceti data, pastrand formatul DD.MM.YY: ')
        tipul = input('Intoduceti tipul cheltuielii, alegand dintre "intretinere", "canal", "alte cheltuieli": ')
        try:
            cheltuieli = add_cheltuiala(cheltuieli, id, nr_ap, suma, data, tipul)
            print('cheltuiala a fost adaugata cu succes')
            return cheltuieli
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')
        finally:
            pass

    def handle_edit_cheltuiala_ui(cheltuieli):
        '''
        Adaugam o cheltuiala citita de la tastatura in lista de cheltuieli
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id = input('Dati ID-ul cheltuielii pe care vreti sa o editati: ')
        nr_ap = input('Dati nr: ')
        suma = input('Dati suma: ')
        data = input('Dati data: ')
        tipul = input('Dati tipul: ')
        try:
            cheltuieli = edit_cheltuiala(cheltuieli, id, nr_ap, suma, data, tipul)
            print('cheltuiala a fost modificata cu succes')
            return cheltuieli
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_delete_cheltuiala_ui(cheltuieli):
        '''
        Stergem cheltuieli din memorie
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id_cheltuiala = input("Dati id-ul cheltuielii care se va sterge: ")
        cheltuieli_new = delete_cheltuiala(cheltuieli, id_cheltuiala)
        print("Stergerea a avut loc cu succes!")
        return cheltuieli_new

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            cheltuieli = handle_add_cheltuiala_ui(cheltuieli)
        elif cmd == '2':
            cheltuieli = handle_edit_cheltuiala_ui(cheltuieli)
        elif cmd == '3':
            cheltuieli = handle_delete_cheltuiala_ui(cheltuieli)
        elif cmd == '4':
            handle_show_all(cheltuieli)
        elif cmd == '5':
            run_console(cheltuieli)
        else:
            print("Comanda invalida")


def run_operatiuni_ui(cheltuieli):
    '''
    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    #def handle_stergere_toate_cheltuieli(cheltuieli):

        #'''
        #Reducerea nr de tipul pentru cheltuielile ce contin un string dat de la tastatura
        #Cu cat se reduc tipulle se citeste de asemenea de la tastatura
        #:param cheltuieli: lista de cheltuieli
        #:return:
        #'''
        #nr_ap = int(input("Dati numarul apartamentului unde vreti sa stergeti toate cheltuielile: "))
        #cheltuieli_new = stergere_toate_cheltuieli(cheltuieli, nr_ap)
        #print("Toate cheltuielile pentru apartamentul introdus au fost sterse cu succes!")
        #return cheltuieli_new

    def handle_add_value(cheltuieli):
        '''
        :param cheltuieli:
        :return:
        '''
        data = input("Introduceti data la care doriti sa adaugati o valoare: ")
        val = float(input("Introduceti valoarea pe care doriti sa o adaugati: "))
        cheltuieli = add_value(cheltuieli, data, val)
        print("Valoarea a fost adaugata cu succes!")
        return cheltuieli

    def handle_sort_cheltuieli(cheltuieli):
        '''
        :param cheltuieli:
        :return:
        '''
        cheltuieli = sort_cheltuieli(cheltuieli)
        print('Ordonarea s-a facut cu succes!')
        return cheltuieli

    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        #if cmd == '1':
            #cheltuieli = handle_stergere_toate_cheltuieli(cheltuieli)
        if cmd == '2':
            cheltuieli = handle_add_value(cheltuieli)
        #if cmd == '3':
            #cheltuieli = handle_biggest_cheltuiala(cheltuieli)
        elif cmd == '4':
            cheltuieli = handle_sort_cheltuieli(cheltuieli)
        #if cmd == '5':
            #cheltuieli = handle_show_sumforap(cheltuieli)
        elif cmd == '6':
            run_console(cheltuieli)
        else:
            print("Comanda invalida")

def run_undo_redo_ui(cheltuieli):
    pass

def run_console(cheltuieli):
    '''
    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(cheltuieli)
        elif cmd == '2':
            run_operatiuni_ui(cheltuieli)
        elif cmd == '3':
            run_undo_redo_ui(cheltuieli)
        elif cmd == 'x':
            break
        elif cmd == "n":
            run_comenzi(cheltuieli)
        else:
            print('Comanda invalida')

def run_undo_redo_ui(cheltuieli):
    pass

def run_console(cheltuieli):
    '''
    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(cheltuieli)
        elif cmd == '2':
            run_operatiuni_ui(cheltuieli)
        elif cmd == '3':
            run_undo_redo_ui(cheltuieli)
        elif cmd == 'x':
            break
        elif cmd == "n":
            run_comenzi(cheltuieli)
        else:
            print('Comanda invalida')