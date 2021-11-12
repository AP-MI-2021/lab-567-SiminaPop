def do_undo(undo_list, redo_list, cheltuieli):
    '''
    :param undo_list:lista cu actiunile facute
    :param redo_list:lista cu actiunile anulate
    '''
    if len(undo_list) > 0:
        undo = undo_list.pop()
        redo_list.append(cheltuieli)
        return undo
    return cheltuieli

def do_redo(undo_list, redo_list, cheltuieli):
    '''
    :params undo_list: lista cu actiunile facute
    :params redo_list: lista cu actiunile anulate
    '''
    if len(redo_list) > 0:
        redo = redo_list.pop()
        undo_list.append(cheltuieli)
        return redo
    return cheltuieli