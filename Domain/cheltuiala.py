def create_cheltuieli(id, numar_apartament, suma, data, tipul):
    '''
    :param id: string
    :param numar_apartament: int
    :param suma: int
    :param data: int
    :param tipul: string
    :return: Dict
    '''

    return {
        "id": id,
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tipul": tipul,
    }

def get_id(cheltuieli):
    '''
    :param cheltuieli: Dict
    :return: id: string
    '''
    return cheltuieli['id']

def set_id(cheltuieli, id):
    '''
    Setarea id la cheltuiala
    :param cheltuiala: Dict
    :param id: string
    :return:
    '''
    cheltuiala['id'] = id

def get_nr_ap(cheltuiala):
    '''
    :param cheltuiala: Dict
    :return: nr_ap: int
    '''
    # return cheltuiala[1]
    return cheltuiala['nr_ap']

def set_nr_ap(cheltuiala, nr_ap):
    '''
    Setarea nr_ap la cheltuiala
    :param cheltuiala: Dict
    :param nr_ap: int
    :return:
    '''
    cheltuiala['nr_ap'] = nr_ap

def get_suma(cheltuiala):
    '''
    :param cheltuiala: Dict
    :return: suma: int
    '''
    # return cheltuiala[2]
    return cheltuiala['suma']

def set_suma(cheltuiala, suma):
    '''
    Setarea suma la cheltuiala
    :param cheltuiala: Dict
    :param suma: int
    :return:
    '''
    cheltuiala['suma'] = suma

def get_data(cheltuiala):
    '''
    :param cheltuiala: Dict
    :return: data: string
    '''
    # return cheltuiala[3]
    return cheltuiala['data']

def set_data(cheltuiala, data):
    '''
    Setarea data la cheltuiala
    :param cheltuiala: Dict
    :param data: string
    :return:
    '''
    cheltuiala['data'] = data

def get_tipul(cheltuiala):
    '''
    :param cheltuiala: Dict
    :return: tipul: string
    '''
    # return cheltuiala[4]
    return cheltuiala['tipul']

def set_tipul(cheltuiala, tipul):
    '''
    Setarea tipul la cheltuiala
    :param cheltuiala: Dict
    :param tipul: string
    :return:
    '''
    cheltuiala['tipul'] = tipul


def to_str(cheltuiala):
    return f'ID={get_id(cheltuiala)}, nr_ap={get_nr_ap(cheltuiala)}, suma={get_suma(cheltuiala)},'\
        f' data={get_data(cheltuiala)}, tipul={get_tipul(cheltuiala)}'