import avg_creator
import file_read
import tkinter as tk


# User-defined data form GUI
data_file_name: str = ""
headers_list: list = []
columns_list: list = []


# GUI data operations - "command" functions
def pass_file_name(text: str):
    """
    command from submit_file_name_button
    After passing correct name, unlock next button, allowing reading data from passed file
    :param text: user input from file_name_text_field
    """
    global data_file_name
    data_file_name = text
    first_label.config(text="teraz plik nazywa się: " + data_file_name)
    commit_file_name_button.config(state="active")


def load_file_data():
    global headers_list, columns_list

    headers_list, columns_list, msg = file_read.read_csv(file_name_text_field.get())

    first_label.config(text=msg)                                                # pass a massege from read.csv function
    commit_file_name_button.config(state="disabled")                            # lock a data load button.

    data_headers_test_msg: str = headers_list                                   # show headers from file
    data_headers_test.insert(0, data_headers_test_msg)

    first_line: str = ""
    for column in columns_list:
        first_line += "{" + str(column[1]) + "}/"
    data_first_record_test_msg: str = first_line + "\n"
    data_first_record_test.config(text=data_first_record_test_msg)              # show first record data

    axis_X_choices_msg.config(state="normal")
    column_X_text_field.config(state="normal")
    column_Y_text_field.config(state="normal")


# Main window configuration
root = tk.Tk()

# Screen geometry - is done like that in case of screen manipulation later
width: int = 1800                                                           # Pixel must be an INT ;-)
height: int = 900
scr_size: str = str(width) + "x" + str(height)

root.geometry(scr_size)
root.title('języki skryptowe - ciągi czasowe wygładzane średnią ruchomą')

# First event
# Message
first_msg: str = "podaj ścieżkę pliku .csv z danymi"
first_label = tk.Label(root, text=first_msg, font=20, fg='black')
first_label.pack()                                                          # def. TOP

# Text field for file name
file_name_text_field = tk.Entry(root)
file_name_text_field.insert(0, "test_csv.csv")                    # init input
file_name_text_field.pack()

# Save new file name on button click
submit_file_name_button = tk.Button(root, text="zatwierdź nazwę pliku",
                                    command=lambda: pass_file_name(file_name_text_field.get()))
submit_file_name_button.pack()

# Load Data from csv file if name is approved
commit_file_name_button = tk.Button(root, text="sprawdź zawartość",
                                    command=load_file_data, state="disabled")
commit_file_name_button.pack()

# msg with file header
data_headers_test = tk.Entry(root, font=16, fg='black')
data_first_record_test = tk.Label(root, text="", font=16, fg='black')
data_headers_test.pack()
data_first_record_test.pack()

# msg about choice column to plot
axis_X_choices_msg_text = "wybierz kolumny do wyświetlenia na wykresie"
axis_X_choices_msg = tk.Label(root, text=axis_X_choices_msg_text, font=20, fg='black', state="disabled")
axis_X_choices_msg.pack()


column_X_text_field = tk.Entry(root, state="disabled")
column_X_text_field.insert(0, "wybierz wartości na oś X")
column_X_text_field.pack()
column_Y_text_field = tk.Entry(root, state="disabled")
column_Y_text_field.insert(0, "wybierz wartości na oś Y")
column_Y_text_field.pack()





# print_plt_button = tk.Button(root, text="generuj wykres wg. kolumn", command= Generuj_Wykres, state="disabled")
# print_plt_button.pack()

root.mainloop()




