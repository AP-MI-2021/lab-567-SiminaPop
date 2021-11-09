from Tests.domain_test import cheltuiala_test
from Tests.test_crud import test_add_cheltuiala, test_edit_cheltuiala, test_delete_cheltuiala
from Tests.operatiuni_test import test_stergere_toate_cheltuieli, test_add_value, test_biggest_cheltuiala, test_ordonare_cheltuieli


def run_all_tests():
    test_add_cheltuiala()
    test_edit_cheltuiala()
    test_delete_cheltuiala()
    test_stergere_toate_cheltuieli()
    test_add_value()
    test_biggest_cheltuiala()
    test_ordonare_cheltuieli()
    cheltuiala_test()