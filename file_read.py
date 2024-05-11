import csv


def read_csv(file_title: str):
    """
    Easiest function for two columns csv reading into lists

    :parameter file_title: str - name of file with data. NOTE it's must be in script directory
    :returns (time_stamp_list, values_list)
    """
    time_stamp_list = []
    values_list = []

    with open(file_title, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            time_stamp_list.append(row[0])
            values_list.append(row[1])

    return time_stamp_list, values_list


if __name__ == '__main__':
    file_name: str = 'test_csv'
    col1, col2 = read_csv(file_name)
    print(col1, col2)
