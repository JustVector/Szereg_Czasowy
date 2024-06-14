#import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import avg_creator as avg


def print_plot(time_stamp_list: list,values_list: list, set_size: int):

    # Convert data from strings list to numpay array, for mtl.plt usage
    values_def_nparr = np.asarray(values_list)
    time_stamp_def_nparr = np.asarray(time_stamp_list)
    values_avg = avg.srednia_ruchoma(values_list, set_size)
    time_stamp_avg = avg.dostosuj_znaczniki(time_stamp_list, set_size)

    values_avg = np.asarray(values_avg)
    time_stamp_avg = np.asarray(time_stamp_avg)
    stamp_list = []
    for i in time_stamp_list:
        if time_stamp_list.index(i) % 24 == 0:
            stamp_list.append(i)

    # Plt Axes configuration
    fig, ax = plt.subplots(2, 1, figsize=(30, 12))
    ax[0].set_ylabel("Wartości")
    ax[0].set_xlabel("Etykiety czasu")

    plt.xticks(rotation=60)
    ax[0].set_title("Ciąg czasowy pobrany z pliku")
    ax[0].set_xticks(np.arange(0, len(time_stamp_avg), len(time_stamp_avg)/len(stamp_list)), stamp_list)
    ax[0].plot(time_stamp_def_nparr, values_def_nparr,  label="Ciąg czasowy pobrany z pliku")

    ax[1].set_ylabel("Wartości")
    ax[1].set_xlabel("Etykiety czasu")

    plt.xticks(rotation=60)
    ax[1].set_xticks(np.arange(0, len(time_stamp_avg), len(time_stamp_avg)/len(stamp_list)), stamp_list)
    ax[1].set_title("Ciąg czasowy wygładzany średnią ruchomą")
    ax[1].plot(time_stamp_avg, values_avg, label="Ciąg czasowy wygładzany średnią ruchomą")

    plt.show()
