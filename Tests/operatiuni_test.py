from Logic.crud import *
from Logic.operatiuni import *
from Domain.cheltuiala import create_cheltuiala


def test_stergere_toate_cheltuieli():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 1, 1, 120.9, '04.06.2002', 'alte cheltuieli', [], [])
    cheltuieli = add_cheltuiala(cheltuieli, 2, 4, 120.9, '04.07.2002', 'alte cheltuieli', [], [])
    cheltuieli = add_cheltuiala(cheltuieli, 3, 4, 145.8, '04.07.2002', 'alte cheltuieli', [], [])
    assert len(cheltuieli) == 3
    cheltuieli = stergere_toate_cheltuieli(cheltuieli, 4, [], [])
    assert len(cheltuieli) == 1

def test_add_value():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 1, 4, 154.35, "23.06.2021", "alte cheltuieli", [], [])
    cheltuieli = add_cheltuiala(cheltuieli, 2, 35, 400, "04.06.2002", "intretinere", [], [])
    cheltuieli = add_cheltuiala(cheltuieli, 3, 124, 98.5, "04.06.2002", "canal", [], [])

    cheltuieli = add_value(cheltuieli, "04.06.2002", 10, [], [])
    assert len(cheltuieli) == 3
    assert get_suma(cheltuieli[0]) == 154.35
    assert get_suma(cheltuieli[1]) == 410
    assert get_suma(cheltuieli[2]) == 108.5

def test_biggest_cheltuiala():
    lista = []
    lista = add_cheltuiala(lista, 'id1', 1, 120.9, '04.06.2002', 'canal', [], [])
    lista = add_cheltuiala(lista, 'id2', 6, 98.4, '04.09.2002', 'alte cheltuieli', [], [])
    lista = add_cheltuiala(lista, 'id3', 6, 198.4, '04.09.2002', 'alte cheltuieli', [], [])
    rezultat = biggest_cheltuiala(lista)

    assert len(rezultat) == 2
    assert rezultat['canal'] == 120.9
    assert rezultat['alte cheltuieli'] == 198.4

def test_ordonare_cheltuieli():
    p1 = create_cheltuiala('id2', 1, 120.9, '04.06.2002', 'alte cheltuieli')
    p2 = create_cheltuiala('id2', 6, 98.4, '04.09.2002', 'alte cheltuieli')
    p3 = create_cheltuiala('id1', 7, 453.5, '04.03.2002', 'alte cheltuieli')

    sorted_list = sort_cheltuieli([p1, p2, p3], [], [])
    assert sorted_list[0] == p3
    assert sorted_list[1] == p1
    assert sorted_list[2] == p2

def test_sume_lunare_ap():
    lista = []
    lista = add_cheltuiala(lista, 'id1', 1, 120.9, '04.06.2002', 'canal', [], [])
    lista = add_cheltuiala(lista, 'id2', 6, 98.4, '04.09.2002', 'alte cheltuieli', [], [])
    lista = add_cheltuiala(lista, 'id3', 6, 198.4, '04.09.2002', 'alte cheltuieli', [], [])
    rezultat_sume = sume_lunare_ap(lista)
    rezultat = {}
    rezultat[3] = [100]
    rezultat[4] = [300, 450, 600, 250]
    assert len(rezultat) == len(rezultat_sume)
    assert rezultat == rezultat_sume