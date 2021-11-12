from UI.consola import run_console
from Tests.run_all_tests import run_all_tests

def main():
    cheltuieli = []
    undo = []
    redo = []
    run_console(cheltuieli, undo, redo)

run_all_tests()
main()