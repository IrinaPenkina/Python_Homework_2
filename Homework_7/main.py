from Seminar_7_task_1 import generate_numbers
from Seminar_7_task_2 import generate_name_file
from Seminar_7_task_3 import read_line_or_begin, process_files
from Seminar_7_task_4 import generate_text, generate_files
from Seminar_7_task_5_6 import generate_with_dictionary
from Seminar_7_task_7 import sort_files
from Seminar_7_task_8_HW import file_rename

if __name__ == '__main__':
    generate_numbers(10, "data_1.txt")
    generate_name_file("data_2.txt", 25)
    process_files("data_1.txt", "data_2.txt", "res.txt")
    generate_files("rnd", "files")
    d = {
        'doc': 5,
        'jpg': 10,
        'png': 23,
        'txt': 15,
    }
    generate_with_dictionary(d)
    sort_files("files")
    file_rename("files", 3, "rnd", "red", [0, 4], "new")

    

