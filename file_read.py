import csv


def read_csv(file_title: str):
    """
    Function reading csv files and write them into lists (one column, one list)
    in case of err, Exception is printed in :msg variable
    :parameter file_title: str - name of file with data. NOTE it's must be in script directory
    :returns (headers_list, values_columns_list, msg)
    """
    headers_list = []
    values_columns_list = []

    try:
        with open(file_title, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in reader:
                if i != 0:                              # if not first row, add each value to its column list
                    column_index = 0
                    for col in row:
                        values_columns_list[column_index].append(col)
                        column_index += 1
                else:
                    headers_list = row                  # headers list
                    column_index = 0                    # Headers in to Columns List
                    for col in row:
                        col_ = [col]
                        values_columns_list.append(col_)
                        column_index += 1
                i += 1

        msg = "wczytano dane: " + str(i) + " wierszy"

    except FileNotFoundError:
        msg = "błąd w trakcie wczytwywania danych: FileNotFoundError "
        return None, None, msg
    except Exception as err:
        msg = "błąd w trakcie wczytwywania danych: " + str(err)
        return None, None, msg

    return headers_list, values_columns_list, msg


def get_data_from_column_list(header: str, headers_list: list, columns_list: list, value: bool = False):
    data: list = []
    msg: str = ""
    float_status: bool = value

    data_indeks = headers_list.index(header)
    file_data: list = columns_list[data_indeks]
    file_data.pop(0)
    print(file_data)

    if float_status == 1:
        for value in file_data:
            try:
                data.append(float(value))
            except ValueError:
                print(value, ": zastąpiono wartością zerową \n")
                data.append(0)
        msg += f"przetwarzanie danych z pliku zakończone sukcesem dla kolumny {header}\n"
    else:
        msg = f"nie przetwarzano danych z pliku dla kolumny {header}\n"
        data = file_data

    return data, msg


if __name__ == '__main__':
    file_name: str = 'test_csv.csv'
    col1, col_list, commit = read_csv(file_name)
    print(commit)
    print(col1, "\n", col_list)
