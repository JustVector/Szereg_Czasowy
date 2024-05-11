import avg_creator
import file_read
import tkinter as tk


# User-defined data form GUI
data_file_name: str = ""
time_stamp_list: list = []
values_list: list = []


# GUI data operations - "command" functions
def pass_file_name(text:str):
    """
    command from submit_file_name_button
    After passing correct name, create new button, allowing reading data from passed file
    :param text: user input from file_name_text_field
    """
    global data_file_name
    data_file_name = text
    first_label.config(text="teraz plik nazywa się: " + data_file_name)

    commit_file_name_button = tk.Button(root, text="zatwierdź nazwę pliku i sprawdź zawartość",
                              command=load_file_data)
    commit_file_name_button.pack()                                                # Load Data from csv file if name is approve


def load_file_data():
    global time_stamp_list, values_list

    time_stamp_list, values_list, msg = file_read.read_csv(file_name_text_field.get())

    first_label.config(text=msg)


# Main window configuration
root = tk.Tk()
    # Screen geometry - is done like that in case of screen manipulation later
width: int = 1800                                                           # Pixel must be an INT ;-)
height: int = 900
scr_size: str = str(width) +"x"+ str(height)

root.geometry(scr_size)
root.title('języki skryptowe - ciągi czasowe wygładzane średnią ruchomą')

    # First event
        # Message
first_msg: str = "podaj ścieżkę pliku .csv z danymi"
first_label = tk.Label(root, text=first_msg, font=20, fg='black')
first_label.pack()                                                          # def. TOP

        # Text field for file name
file_name_text_field = tk.Entry(root)
file_name_text_field.insert(0, "nazwa pliku")                                  # init input
file_name_text_field.pack()

        # Save new file name on button click
submit_file_name_button = tk.Button(root, text="zatwierdź nazwę pliku",
                                    command=lambda: pass_file_name(file_name_text_field.get()))
submit_file_name_button.pack()

#print_plt_button = tk.Button(root, text="generuj wykres", command= Generuj_Wykres)
#print_plt_button.pack()

root.mainloop()




