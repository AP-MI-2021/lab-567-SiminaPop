from Domain.cheltuiala import *

def cheltuiala_test():
    cheltuiala = create_cheltuiala('id', 'nr_ap', 'suma', 23.45, 240)
    assert get_id(cheltuiala) == 'id'
    assert get_nr_ap(cheltuiala) == 'nr_ap'
    assert get_suma(cheltuiala) == 'suma'
    assert get_data(cheltuiala) == 23.45
    assert get_tipul(cheltuiala) == 240

    set_id(cheltuiala, 'id2')
    set_nr_ap(cheltuiala, 'nr_ap2')
    set_suma(cheltuiala, 'suma2')
    set_data(cheltuiala, 50.5)
    set_tipul(cheltuiala, 300)

    assert get_id(cheltuiala) == 'id2'
    assert get_nr_ap(cheltuiala) == 'nr_ap2'
    assert get_suma(cheltuiala) == 'suma2'
    assert get_data(cheltuiala) == 50.5
    assert get_tipul(cheltuiala) == 300