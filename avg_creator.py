"""!UTF-8"""


def srednia_ruchoma(data_list:list, set_size:int ):
    """Funkcja przetwarzająca podaną listę data_list na ciąg liczb (float)
     które odpowiadja średniej kolejnych n(=set_size) liczb z listy
     data_list:list = przyjmuje listę wartości (np z ciagu czasowego
     set_size:int = przyjmuje ilość kolejnych liczb z których ma być liczona średnia. MUSI BYĆ NIEPARZYSTA
     """
    set_range: int = set_size//2
    list_size: int = len(data_list)
    avg_list: list = []

    if set_size % 2 == 0:
        raise ValueError("Set_Size MUST be odd")

    for index in range(0,list_size):
        mid_list = []
        if index == 0:
            pass
        elif index + set_range == list_size:
            pass
        else:
            avg_val = 0
            for i in range(-set_range, set_range):
                avg_val += data_list[index+i]

            avg_val = avg_val/set_size
            avg_list.append(avg_val)
    return avg_list


if __name__ == '__main__':
    data = [112, 124, 322, 45, 324, 223, 234, 233, 535, 353, 535, 334, 531, 241]
    set_size: int = 4  # liczba nieparzysta!

    print(srednia_ruchoma(data, set_size))