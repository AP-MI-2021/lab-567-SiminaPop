from Logic.crud import add_cheltuiala, delete_cheltuiala
from Logic.Undo_Redo import do_undo, do_redo


def test_undo_redo_sep():
    cheltuiala = []
    undo_list = [[]]
    redo_list = []
    cheltuiala = add_cheltuiala(cheltuiala, 'id1', 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    assert len(cheltuiala) == 1
    cheltuiala = delete_cheltuiala(cheltuiala, 'id1', undo_list, redo_list)
    assert len(cheltuiala) == 0
    cheltuiala = do_undo(undo_list, redo_list, cheltuiala)
    assert len(cheltuiala) == 1
    cheltuiala = do_redo(undo_list, redo_list, cheltuiala)
    assert len(cheltuiala) == 0


def test_undo_redo():
    start_program = []
    undo_list = [[]]
    redo_list = []
    start_program = add_cheltuiala(start_program, 'id1', 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    assert len(start_program) == 1
    start_program = add_cheltuiala(start_program, 'id2', 126, 220, '12-10-2021', 'alte cheltuieli', undo_list,
                                   redo_list)
    assert len(start_program) == 2
    start_program = add_cheltuiala(start_program, 'id3', 128, 420, '13-10-2021', 'intretinere', undo_list,
                                   redo_list)
    assert len(start_program) == 3
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = add_cheltuiala(start_program, 'id1', 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    start_program = add_cheltuiala(start_program, 'id2', 126, 220, '12-10-2021', 'alte cheltuieli', undo_list,
                                   redo_list)
    start_program = add_cheltuiala(start_program, 'id3', 128, 420, '13-10-2021', 'intretinere', undo_list,
                                   redo_list)
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 3
    start_program = do_undo(undo_list, redo_list, start_program)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 3
    start_program = do_undo(undo_list, redo_list, start_program)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = add_cheltuiala(start_program, 'id4', 128, 420, '14-10-2021', 'intretinere', undo_list, redo_list)
    assert len(start_program) == 2
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = do_redo(undo_list, redo_list, start_program)
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2