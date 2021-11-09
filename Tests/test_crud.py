from Logic.crud import add_cheltuiala, edit_cheltuiala, find_cheltuiala, delete_cheltuiala
from Domain.cheltuiala import create_cheltuiala, get_id, get_nr_ap, get_suma, get_data, get_tipul


def test_add_cheltuiala():
    cheltuieli = []
    cheltuiala_adaugata = create_cheltuiala('12389', 1, 123.6, '12.12.2020', 'canal')
    cheltuieli = add_cheltuiala(cheltuieli, '12389', 1, 123.6, '12.12.2020', 'canal')
    assert len(cheltuieli) == 1
    assert cheltuieli[0] == cheltuiala_adaugata
    assert get_id(cheltuieli[0]) == '12389'
    assert get_nr_ap(cheltuieli[0]) == 1
    assert get_suma(cheltuieli[0]) == 123.6
    assert get_data(cheltuieli[0]) == '12.12.2020'
    assert get_tipul(cheltuieli[0]) == 'canal'

    cheltuieli = add_cheltuiala(cheltuieli, '123', 2, 234.4, '01.09.2019', 'intretinere')
    cheltuiala_adaugata_2 = create_cheltuiala('123', 2, 234.4, '01.09.2019', 'intretinere')
    assert len(cheltuieli) == 2
    assert cheltuieli[0] == cheltuiala_adaugata
    assert cheltuieli[1] == cheltuiala_adaugata_2


def test_edit_cheltuiala():
    p1 = create_cheltuiala('12389', 1, 123.6, '12.12.2020', 'canal')
    p2 = create_cheltuiala('12389', 1, 245.7, '12.12.2020', 'canal')
    cheltuieli = [p1, p2]
    assert len(cheltuieli) == 2
    cheltuieli = edit_cheltuiala(cheltuieli, '12389', 1, 567.9, '12.12.2020', 'canal')
    assert len(cheltuieli) == 2
    p1_new = find_cheltuiala(cheltuieli, '12389')
    assert get_id(p1_new) == '12389'
    assert get_nr_ap(p1_new) == 1
    assert get_suma(p1_new) == 567.9
    assert get_data(p1_new) == '12.12.2020'
    assert get_tipul(p1_new) == 'canal'

    try:
        cheltuieli = edit_cheltuiala(cheltuieli, '12389', '', 'cheltuiala new', 'jhdfsj', '-2154')
        assert False
    except ValueError:
        assert True

def test_delete_cheltuiala():
    p1 = create_cheltuiala('12389', 1, 123.6, '12.12.2020', 'canal')
    p2 = create_cheltuiala('12325', 4, 300.6, '12.09.2020', 'intretinere')
    cheltuieli = [p1, p2]
    assert len(cheltuieli) == 2
    cheltuieli = delete_cheltuiala(cheltuieli, '12389')
    assert len(cheltuieli) == 1
    cheltuieli = delete_cheltuiala(cheltuieli, '12d456')
    assert len(cheltuieli) == 1
