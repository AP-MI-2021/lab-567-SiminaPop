def create_cheltuiala(id, nr_ap, suma, data, tipul):
    '''
    :param id: string
    :param nr_ap: int
    :param suma: float
    :param data: int
    :param tipul: string
    :return: Dict
    '''

    return {
        "id": id,
        "nr_ap": nr_ap,
        "suma": suma,
        "data": data,
        "tipul": tipul,
    }

def get_id(cheltuiala):
    '''
    :param cheltuiala: Dict
    :return: id: string
    '''
    return cheltuiala['id']

def set_id(cheltuiala, id):
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